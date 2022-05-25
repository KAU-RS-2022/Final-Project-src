var make_survey = function(id){
    // console.log(1);
    console.log(id);
    let list;
    $.ajax({
        type : "POST",
        url : "/test",
        async : false,
        success: function(data){
            console.log(data);
            list = data;
        },
        error : function(a, b, c){
            console.log('error');
        }
    });

    let html = `아이디 : <input type='text' name="id" id='user_id'><br><br>`
    let number, question;

    for (let i = 0 ; i < list.length ; i++){
        // console.log(list[i]);
        number = list[i].idx;
        question = list[i].question;
        type = list[i].type;

        html += `
            ${number}. ${question}
            
        `
        if(type=='sex'){
            html+=`<br>
            <input type="radio" name="A${number}" id="A${number}_male" value="male" checked><label for="A${number}_male">남자</label>
            <input type="radio" name="A${number}" id="A${number}_female" value="female"><label for="A${number}"_female>여자</label><br><br>
            `
        }
        else if(type=='age'){
            html+=`
            <input type="number" name="A${number}" min="1" max="99" value="24">살<br><br>
            `
        }
        else if (type=='5'){
            html+=`<br>
            <input type="radio" name="A${number}" id="A${number}_1" value="1"><label for="A${number}_1">매우 싫어함</label>
            <input type="radio" name="A${number}" id="A${number}_2" value="2"><label for="A${number}_2">싫어함</label>
            <input type="radio" name="A${number}" id="A${number}_3" value="3" checked><label for="A${number}_3">보통</label>
            <input type="radio" name="A${number}" id="A${number}_4" value="4"><label for="A${number}_4">좋아함</label>
            <input type="radio" name="A${number}" id="A${number}_5" value="5"><label for="A${number}_5">매우 좋아함</label><br><br>
            `
        }
        else if (type=='skill'){
            html+=`<br>
            <input type="radio" name="A${number}" id="A${number}_1" value="아무나"><label for="A${number}_1">아무나</label>
            <input type="radio" name="A${number}" id="A${number}_2" value="초급"><label for="A${number}_2">초급</label>
            <input type="radio" name="A${number}" id="A${number}_3" value="중급" checked><label for="A${number}_3">중급</label>
            <input type="radio" name="A${number}" id="A${number}_4" value="고급"><label for="A${number}_4">고급</label>
            <input type="radio" name="A${number}" id="A${number}_5" value="신의경지"><label for="A${number}_5">신의경지</label><br><br>
            `
        }
        else if (type=='time'){
            html+=`<br>
            <input type="radio" name="A${number}" id="A${number}_1" value="15분 이내"><label for="A${number}_1">15분 이내</label>
            <input type="radio" name="A${number}" id="A${number}_2" value="30분 이내"><label for="A${number}_2">30분 이내</label>
            <input type="radio" name="A${number}" id="A${number}_3" value="60분 이내" checked><label for="A${number}_3">60분 이내</label>
            <input type="radio" name="A${number}" id="A${number}_4" value="90분 이내"><label for="A${number}_3">90분 이내</label>
            <input type="radio" name="A${number}" id="A${number}_5" value="120분 이내"><label for="A${number}_4">120분 이내</label><br><br>
            `
        }
        // 여러개 선택
        else{
            type = type.split(',');
            // console.log(type)
            for(let j = 0 ; j < type.length ; j++){
                if (j%5==0){
                    html+=`<br>`
                }
                html+=`
                <input type="checkbox" name="A${number}" id="A${number}_1" value="${type[j]}"><label for="A${number}_1">${type[j]}</label>
                `
            }
            html+=`<br><br>`
        }
    }
    html+=`
        <input type="submit" value="전송">
    `
    $('#surveys').html(html);    
}