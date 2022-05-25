const spawn = require('child_process').spawn;

const result = spawn('python', ['RECIPE.py', '10']); 

result.stdout.on('data', function(data) { 
    list = data.toString();
    
    list = list.split('\n');
    list.pop();

    console.log(list);
    var menu;
    for (let i = 0 ; i < list.length ; i++){
        menu = list[i].split(' ')[0];
        console.log(Number(menu))
    }

}); 

// 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다. 
result.stderr.on('data', function(data) { 
    console.log(data.toString()); 
});