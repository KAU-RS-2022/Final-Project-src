function split_list(a){
    let end_list = [];
    
    //있으면 ( 여러개 )
    if(a.indexOf(',')+1){
        for(let i = 0 ; i < a.split(',').length ; i++){
            end_list.push(a.split(',')[i]);
        }
    }
    //없으면( 1개 )
    else{
        end_list.push(a);
    }

    // console.log(end_list);
    return end_list;
}

var recommend_recipe = function(id, rcp_sno_list){
    let recipe_list;
    $.ajax({
        type : "POST",
        url : "/recipe/recommend",
        async : false,
        data : {
            list: rcp_sno_list
        },
        success: function(data){
            recipe_list = data;
            console.log(recipe_list);
        },
        error : function(a, b, c){
            console.log('error');
        }
    });

    let ref_list = '';
    let ref;
    $.ajax({
        type : "POST",
        url : "/recipe/my_ref",
        async : false,
        data : {
            id: id
        },
        success: function(data){
            ref = data;
            console.log(ref);
        },
        error : function(a, b, c){
            console.log('error');
        }
    });

    ref_list += ref.fruit+',';
    ref_list += ref.etc+',';
    ref_list += ref.meat+',';
    ref_list += ref.dairy+',';
    ref_list += ref.seafood;


    ref_list = ref_list.split(',')
    console.log(ref_list);

    let html = `
        <tr>
            <th>요리</td>
            <th>재료</td>
        </tr>
    `
    
    var recipe_num, recipe_name, recipe_material;
    var turn_continue;


    //있는 재료 pass 없는 재료 ㅈ까

    for (let i = 0 ; i < recipe_list.length ; i++){
        turn_continue = false;
        recipe_num = recipe_list[i].rcp_sno;    //번호
        recipe_name = recipe_list[i].ckg_nm;           //요리이름
        recipe_material = recipe_list[i].ckg_mtrl_cn;  //요리재료
        recipe_type = recipe_list[i].ckg_mtrl_acto_nm  //류


        // 재료 2개 이상인 것만 출력하도록
        let ing_cnt = 0;
        for(let j = 0 ; j<ref_list.length ; j++){
            // 없으면 -1 있으면 해당 index
            // 있을 때
            if(recipe_material.indexOf(ref_list[j])+1){
                ing_cnt += 1;
            }
        }

        if (ing_cnt < 2){
            continue;
        }
        // console.log(recipe_name);

        html+=`
            <tr>
                <td class="food_name"><a href=https://www.10000recipe.com/recipe/${recipe_num} style="color:red;">${recipe_name}</a></td>
                <td class="nn">${recipe_material}</td>
            </tr>
        `

    }
    $('#recipe_table').html(html);    
}



var make_recipe = function(){
    let recipe_list;
    let user_answer;

    $.ajax({
        type : "POST",
        url : "/survey/answer",
        async : false,
        data:{
            id: 'whddnbae'
        },
        success: function(data){
            // console.log(data[0]);
            user_answer = data[0];
        },
        error : function(a, b, c){
            console.log('error');
        }
    });

    var difficulty = user_answer.a8;
    var time = user_answer.a9;
    var favorite_type = user_answer.a10;
    var hate = user_answer.a11;
    var allergy = user_answer.a12;

    favorite_type = split_list(favorite_type);
    hate = split_list(hate);
    allergy = split_list(allergy);

    $.ajax({
        type : "POST",
        url : "/recipe/list",
        async : false,
        data : {
            favorite: favorite_type
        },
        success: function(data){
            // console.log(data);
            recipe_list = data;
        },
        error : function(a, b, c){
            console.log('error');
        }
    });


    // console.log(hate);
    let html = `
        <tr>
            <th>요리</td>
            <th>재료</td>
        </tr>
    `
    
    var recipe_num, recipe_name, recipe_material;
    var turn_continue;

    for (let i = 0 ; i < recipe_list.length ; i++){
        turn_continue = false;
        recipe_num = recipe_list[i].rcp_sno;    //번호
        recipe_name = recipe_list[i].ckg_nm;           //요리이름
        recipe_material = recipe_list[i].ckg_mtrl_cn;  //요리재료
        recipe_type = recipe_list[i].ckg_mtrl_acto_nm  //류

        // 알레르기 있는 재료 건너 뛰기
        if(allergy[0] != 'undefined'){
            // console.log(allergy[0]);
            for (let j = 0 ; j < allergy.length ; j++){
                if(recipe_material.indexOf(allergy[j])+1 || recipe_type.indexOf(allergy[j])+1){
                    // console.log(1);
                    turn_continue = true;
                    continue;
                }
            }
            if(turn_continue){
                continue
            }
        }
        // 싫어하는거 건너 뛰기
        if(hate[0] != 'undefined'){
            for (let j = 0 ; j < hate.length ; j++){
                if(recipe_material.indexOf(hate[j])+1 || recipe_type.indexOf(hate[j])+1){
                    // console.log(2);
                    turn_continue = true;
                    continue;
                }
            }
            if(turn_continue){
                continue;
            }
        }


        // console.log(recipe_name);

        html+=`
            <tr>
                <td class="food_name"><a href=https://www.10000recipe.com/recipe/${recipe_num} style="color:red;">${recipe_name}</a></td>
                <td class="nn">${recipe_material}</td>
            </tr>
        `

    }
    $('#recipe_table').html(html);    
}