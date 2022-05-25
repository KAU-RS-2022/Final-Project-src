const fs = require('fs');
const express = require('express');
const cors = require('cors');
const multer = require('multer');
const {Client} = require('pg');
const pg = require('pg');
const spawn = require('child_process').spawn;

const pool = new pg.Pool({
    user : 'jwbae',
    host : 'localhost',
    database : 'rs',
    password : '',
    port : 5433
});


var db = new Client({
    user : 'jwbae',
    host : 'localhost',
    database : 'rs',
    password : '',
    port : 5433
}); 

db.connect();

var app = express();
app.use(express.json({
    limit: '1mb'
}));
app.use(express.urlencoded({ 
    limit: '1mb',
    extended: false 
}));
app.use(express.static('data'));
app.use(cors());
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

function makeFolder(dir) {
    if(!fs.existsSync(dir)){
        fs.mkdirSync(dir);
    }
}


const upload = multer({
    storage: multer.diskStorage({
        destination: function (req, file, cb) {
            let id = req.body.id;
            makeFolder(`${__dirname}/data/receipt`);
            cb(null, `${__dirname}/data/receipt/`);
        },
        filename: function (req, file, cb) {
            // console.log(req.body);
            let id = req.body.id;
            let timestamp = new Date().getTime().valueOf();
            // console.log(timestamp)
            // let name = file.fieldname.slice(4)
            cb(null, `${id}_${timestamp}.png`);
        }
    }),
});

app.get('/', (request, response) => {
    var title = 'HomePage';
    
    response.render('loginindex.ejs');
});

app.get('/ref_content/meat-ref', (req, res) => {
    res.render('ref_content/meat-ref.ejs');
    // res.render('ref_content/meat-ref.ejs');
});
app.get('/ref_content/seafood-ref', (req, res) => {
    res.render('ref_content/seafood-ref.ejs');
});
app.get('/ref_content/dairy-ref', (req, res) => {
    res.render('ref_content/dairy-ref.ejs');
});
app.get('/ref_content/etc-ref', (req, res) => {
    res.render('ref_content/etc-ref.ejs');
});
app.get('/ref_content/fruit-ref', (req, res) => {
    res.render('ref_content/fruit-ref.ejs');
});

app.post('/login_process', (req, res) => {
    var post = req.body;
    var id = post.id;
    var pw = post.pw;

    db.query(`select * from public.user where id='${id}';`, (err, res2) => {
        if (err) { throw err; }
        // console.log(res2.rows[0]);
        try{
            if(res2.rows[0].id == id & res2.rows[0].pw == pw){
                if(res2.rows[0].survey == 'O'){
                    res.redirect('/my_ref');
                }
                else{
                    res.redirect(`/survey?id=${id}`);
                }
            }
            else{
                res.send('등록되지 않은 ID 또는 PW입니다.');
            }
        }
        catch{
            res.send('에러입니다. 다시 접속 해주세요');
        }
    });

    
});


app.get('/home', (req, res) => {
    res.render('home.ejs');
});

app.get('/recipe', (req, res) => {
    res.render('recipe.ejs');
});

app.post('/recipe/list', (req, res) => {
    var favorite = req.body["favorite[]"];
    var results = [];
    

    pool.connect( async (err, client) => {
        if (err) {
            console.log(err);
        } else {
            for(let i = 0 ; i < favorite.length; i++){
                try {
                    var result = await client.query(`select * from recipe WHERE CKG_MTRL_ACTO_NM = '${favorite[i]}' order by inq_cnt desc limit 3;`);
                }  catch (err)  {
                    console.log(err.stack);
                }
    
                results = [...results, ...result.rows]
                // console.log(i)
                // console.log(results);
            }

            
            res.send(results);
            // try {
            //     var result = await client.query(`select * from recipe WHERE CKG_MTRL_ACTO_NM = '가공식품류' order by inq_cnt desc limit 5;`);
            // }  catch (err)  {
            //     console.log(err.stack);
            // }

            // results = [...results, ...result.rows]

            // try {
            //     var result = await client.query(`select * from recipe WHERE CKG_MTRL_ACTO_NM = '닭고기' limit 5;`);
            // }  catch (err)  {
            //     console.log(err.stack);
            // }

            // results = [...results, ...result.rows]

            // console.log(results);
            // hands = Object.keys(hands_json)
            // for (j = 0 ; j < hands.length ; j++){
            //     hand = hands_json[hands[j]];
            //     fingers = Object.keys(hand);
            //     console.log(fingers);
            //     for (k = 0 ; k < fingers.length ; k++){
            //         console.log(hands[j]+'_'+fingers[k])
            //         db.query(`UPDATE config_check SET ${hands[j]+'_'+fingers[k]} = 'o' WHERE id = '${id}';`, (err, res2) => {
            //             if (err) { throw err; }
            //         });
            //     }
            // }
        }
    });




    // // DB전송할때 영어 대문자가 안되네
    // db.query(`select * from recipe WHERE CKG_MTRL_ACTO_NM = '가공식품류' limit 5;`, (err, res2) => {
    //     if (err) { throw err; }
    //     console.log(res2.rows);
    //     result.push(res2.rows);
    // });

    // db.query(`select * from recipe WHERE CKG_MTRL_ACTO_NM = '닭고기' limit 5;`, (err, res2) => {
    //     if (err) { throw err; }
    //     console.log(res2.rows);
    //     result.push(res2.rows);
    // });
    // console.log(1);
    // console.log(result);
    // res.send(result);
});

app.post('/survey/answer', (req, res) => {
    var id = req.body.id;
    db.query(`select * from answer where id='${id}';`, (err, res2) => {
        if (err) { throw err; }
        res.send(res2.rows);
    });
});

app.get('/my_ref', (req, res) => {
    let id = 'tester'
    res.render('my_ref.ejs', {id: id});
});

app.get('/setting', (req, res) => {
    res.render('setting.ejs');
});

app.get('/survey', (req, res) => {
    var id = req.query.id;
    res.render('survey.ejs',{id: id});
});
app.get('/test', (req, res) => {
    var id = req.query.id;
    res.render('test.ejs',{id: id});
});

app.post('/survey', (req, res) => {
    db.query(`select * from survey order by idx ASC;`, (err, res2) => {
        if (err) { throw err; }
        res.send(res2.rows);
    });
});

app.post('/ref_content/type', (req, res) => {
    var id = req.body['id'];
    var type = req.body['type'];
    // console.log(id,type);
    db.query(`select ${type} from refrigerator where id = '${id}';`, (err, res2) => {
        if (err) { throw err; }
        // console.log(res2.rows[0]);
        res.send(res2.rows[0]);
    });
});

app.post('/ref_content/add_del', (req, res) => {
    var id = req.body['id'];
    var type = req.body['type'];
    var ings = req.body['ings'];
    // console.log(id,type, ings);


    // db.query(`select ${type} from refrigerator where id = '${id}';`, (err, res2) => {
    db.query(`update refrigerator set  ${type} = '${ings}' where id = '${id}';`, (err, res2) => {
        if (err) { throw err; }
        // console.log(res2.rows[0]);
        res.send('success');
    });
});

app.post('/test', (req, res) => {
    db.query(`select * from survey order by idx ASC;`, (err, res2) => {
        if (err) { throw err; }
        res.send(res2.rows);
    });
});

app.post('/recipe/rs_model', (req, res) => {
    let id = req.body.id;
    // console.log(id);
    let num;
    db.query(`select id_num from public.answer where id = '${id}';`, (err, res2) => {
        if (err) { throw err; }
        num = res2.rows[0].id_num;
        const result = spawn('python', ['RECIPE.py', num]); 

        result.stdout.on('data', function(data) { 
            list = data.toString();
            
            list = list.split('\n');
            list.pop();
    
            console.log(list);
            var menu;
            var rcp_sno_list = [];
            for (let i = 0 ; i < list.length ; i++){
                menu = list[i].split(' ')[0];
                rcp_sno_list.push(Number(menu))
            }
            res.send(rcp_sno_list);
        }); 
    
        // 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다. 
        result.stderr.on('data', function(data) { 
            console.log(data.toString()); 
        });
    });
});


app.post('/recipe/recommend', (req, res) => {
    let rcp_sno_list = req.body['list[]'];
    console.log(rcp_sno_list);
    let db_where = ''
    for(let i = 0 ; i < rcp_sno_list.length ; i++){
        db_where = db_where + `rcp_sno = '${rcp_sno_list[i]}' or `
        // console.log(rcp_sno_list[i]);
    }
    db_where = db_where.slice(0,-4);
    // console.log(db_where);
    db.query(`select * from public.recipe where ${db_where};`, (err, res2) => {
        if (err) { throw err; }
        res.send(res2.rows);
    });
});


app.post('/recipe/my_ref', (req, res) => {
    let id = req.body.id;
    console.log(id);
    db.query(`select * from public.refrigerator where id = '${id}';`, (err, res2) => {
        if (err) { throw err; }
        // console.log(res2.rows);
        res.send(res2.rows[0]);
    });
});


app.post('/survey/form', (req, res) => {
    console.log(req.body);
    let answers = req.body;
    console.log(answers);
    console.log(answers.A11);

    db.query(`INSERT INTO answer ( id, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 ) 
                VALUES( '${answers.id}', '${answers.A1}', '${answers.A2}', '${answers.A3}', 
                    '${answers.A4}', '${answers.A5}', '${answers.A6}', '${answers.A7}', 
                    '${answers.A8}', '${answers.A9}', '${answers.A10}', '${answers.A11}'
                    , '${answers.A12}'
                )`, (err, res2) => {
        if (err) { throw err; }
    });

    db.query(`update public.user set survey='O' where id='${req.body.id}';`, (err, res2) => {
        if (err) { throw err; }
        // res.send(res2.rows);
    });
    

    // 사용자 id를 같이 받아와서 db에 저장
    res.redirect('/my_ref');
});


app.post('/test/form', (req, res) => {
    console.log(req.body);
    let answers = req.body;
    console.log(answers);
    console.log(answers.A11);
    db.query(`select count(*) from public.answer;`, (err, res2) => {
        if (err) { throw err; }
        console.log(res2.rows[0].count*1+1);
        
        db.query(`INSERT INTO answer ( id_num, id, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 ) 
        VALUES( '${res2.rows[0].count*1+1}', '${answers.id}', '${answers.A1}', '${answers.A2}', '${answers.A3}', 
            '${answers.A4}', '${answers.A5}', '${answers.A6}', '${answers.A7}', 
            '${answers.A8}', '${answers.A9}', '${answers.A10}', '${answers.A11}'
            , '${answers.A12}'
        )`, (err, res3) => {
            if (err) { throw err; }
            res.send('<a href="/test">다시하기</a>');
        });

    });

});


app.listen(3000, () => {
    console.log('Example app listening on port 3000!')
});