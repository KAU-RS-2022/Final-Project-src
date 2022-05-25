import styled from '@emotion/styled';
import React, { useEffect, useState } from 'react'
import DangerElement from '../features/DangerElement/DangerElement';
import SkinTon from '../features/SkinTon/SkinTon';
import SkinTrouble from '../features/SkinTrouble/SkinTrouble';
import SkinType from '../features/SkinType/SkinType';
import { Dispatch, SetStateAction } from 'react'
import { Progress } from 'antd';

export interface SetPageProps {
  _setPage: Dispatch<SetStateAction<number>>
}

const Question = () => {
  const [page, setPage] = useState<number>(1);
  const [question, setQuestion] = useState('내 피부타입은?');

  useEffect(() => {
    if(page === 1) {
      setQuestion('내 피부타입은?');
    } else if(page === 2) {
      setQuestion('내 피부톤은?');
    } else if(page === 3) {
      setQuestion('나의 피부고민은?');
    } else if(page === 4) {
      setQuestion('화장품에 들어가면 안되는 성분은?');
    }
  },[page])

  return (
    <QuestionWrap>
      <div style={{display:'flex', flexDirection:'column', alignItems:'center'}}>
        <div className='questionNum'>Q{page}</div>
        <div className='question'>{question}</div>
        { page === 1 && <SkinType _setPage={setPage} /> }
        { page === 2 && <SkinTon _setPage={setPage} /> }
        { page === 3 && <SkinTrouble _setPage={setPage} /> }
        { page === 4 && <DangerElement /> }

        <Progress 
          style={{
            marginTop:'100px',
            width:'300px'
          }}
          percent={20*page}
          strokeColor='#00FFAB'
          showInfo={false} />
      </div>
    </QuestionWrap>
  )
}

export default Question;

const QuestionWrap = styled.div`
  background-color:#439757;
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  justify-content: center;
  align-items: center;
  color:white;

  .questionNum {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 10px;
  }
  .question {
    font-size: 32px;
    font-weight: 500;
    margin-bottom: 90px;
  }
`;

