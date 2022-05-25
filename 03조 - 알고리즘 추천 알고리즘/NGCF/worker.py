def worker(procnum, count, user_df, problem_df, user_problem_df, return_dict):
    try:
        for i in range(count, count + user_problem_df['userId'].size):
            x = int(user_df[user_df['user_id'] == user_problem_df['userId'][i]]['remap_id'])
            y = int(problem_df[problem_df['problem_id'] == user_problem_df['problemId'][i]]['remap_id'])
            user_problem_df['userId'][i] = x
            user_problem_df['problemId'][i] = y
        return_dict[procnum] = user_problem_df
    except IndexError:
        return_dict[procnum] = user_problem_df
    print('finish')
