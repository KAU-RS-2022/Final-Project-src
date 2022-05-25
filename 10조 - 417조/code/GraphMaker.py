import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv

DATA_PATH = './LightGCN-PyTorch-master/data/'
DATA_LIST = ['amazon-book', 'gowalla', 'yelp2018']
FILE_TRAIN = 'train.txt'
FILE_USER = 'user_list.txt'
N_USER = 20
N_USER_TOSHOW = 10

# 전체 사용자 수, 전체 item 수, 전체 연결된 egde 수

# parameter : data (folder name -> DATA_LIST's element)
def rebuildData(data):
    # will merge user_fle and train_file by remap_id, and remove remap_id to use org_id only.
    train_file = DATA_PATH + data + '/' + FILE_TRAIN
    user_file = DATA_PATH + data + '/' + FILE_USER

    total_dict = {}

    print('Reading original file...')

    # read raw train file
    with open(train_file) as f:
        for l in f.readlines():
            if len(l) > 0:
                l = l.strip('\n').split(' ')
                items = [int(i) for i in l[1:]] # read items
                uid = int(l[0]) # read user id (raw train file's uid is number starts with 0.)

                total_dict[uid] = items
    
    print('Making new file from original file...')

    # Make dataframe from dictionary
    total_df = pd.DataFrame(enumerate(total_dict.items()))

    # Each column means remap_id(transformed user's id) and user's interacted id.
    total_df.rename(columns={0:'remap_id', 1:'item'}, inplace=True)

    # Extract exact items only.
    total_df['item'] = total_df['item'].apply(lambda x: (x[1:])[0])

    # Calculate # of user's interacted items. (for slicing items)
    total_df['item_length'] = total_df['item'].apply(lambda x: len(x))

    # Remove str-like annotations & add ',' for comfortable splitting.
    total_df['item'] = total_df['item'].apply(lambda x: str(x).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', ','))

    user_df = pd.read_csv(user_file, sep=' ') # Load user's information file
    new_df = pd.merge(user_df, total_df) # Merge both files,
    new_df.drop(columns=['remap_id'], axis=1, inplace=True) # and drop remap_id. (will use org_id only)

    threshold = new_df['item_length'].min() + 4 # set slicing threshold

    new_df.drop(new_df[new_df['item_length'] > threshold].index, inplace=True) # Drop user overs item_length threshold.
    new_df.drop(columns=['item_length'], axis=1, inplace=True) # No need to keep item_length column, so drop it.
    new_df = new_df.iloc[:N_USER] # Select users with number of users.

    # Save rebuilded file.
    filePath = DATA_PATH + data + '/' + f'{data}_{N_USER}user.txt'
    new_df.to_csv(filePath, sep=' ', index=False, header=False, quoting=csv.QUOTE_NONE, escapechar='')

    print('Data rebuilding finished...')
    return filePath

def graphMaker(file:str):
    train_file = file
    total_dict = {}

    # User flag (to show)
    flag = 0
    with open(train_file) as f:
        for l in f.readlines():
            if len(l)>0:
                l = l.strip('\n').replace(',', ' ').split(' ')
                items = [int(i) for i in l[1:]]
                uid = l[0] # Now, uid is true (string) id.

                total_dict[uid] = items

                flag += 1
                if flag == N_USER_TOSHOW:
                    break
    
    user_node = list(total_dict.keys()) # remember user node.
    # item_node = list(total_dict.values())

    print('Making Graph from rebuilded file...')
    G = nx.convert.from_dict_of_lists(total_dict) # generate graph from dictionary.

    colormap = []
    for node in G:
        if type(node) == str:
            colormap.append('red') # color user node as red.
        else:
            colormap.append('#1f78b4') # color item node as default.
    
    deg = dict(G.degree()) # remember node's degree. (to resizing)

    pos = nx.bipartite_layout(G, nodes=user_node, align='vertical') # make graph as bipartite graph.

    plt.figure(figsize=(25, 25))

    nx.draw_networkx(
        G,
        pos = pos,
        node_color = colormap,
        node_size = [v * 50 for v in deg.values()],
        with_labels = False,
    )
    
    #plt.show()
    #plt.legend()
    # filename = file.split('/')[-1:][0].split('.')[0].split('_')[0]
    # plt.title(f'Bipartite Graph of {filename} Dataset', fontsize=20)
    
    # save graph image file
    plt.savefig(DATA_PATH + '/[graphimgs]/' + file.split('/')[-1:][0].split('.')[0].split('_')[0] + f'_{flag}user.png', 
                bbox_inches='tight')
    print('Saving graph figure finished...')

filePath = rebuildData(DATA_LIST[1])
# print(filePath)
graphMaker(filePath)