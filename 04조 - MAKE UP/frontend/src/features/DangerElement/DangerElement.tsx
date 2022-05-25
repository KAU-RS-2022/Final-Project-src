import styled from '@emotion/styled';
import React, { useState } from 'react'
import { motion } from "framer-motion"
import { useNavigate } from 'react-router-dom';
import { ButtonItemWrap } from '../SkinTrouble/SkinTrouble';


const DangerElement = () => {
const [ dangerElementList, setDangerElementList ] = useState([
  {
    idx: 1,
    name: '글리세린',
    isClicked: false
  },
  {
    idx: 2,
    name: '정제수',
    isClicked: false
  },
  {
    idx: 3,
    name: '부틸렌글라이콜',
    isClicked: false
  },
  {
    idx: 4,
    name: '12헥산다이올',
    isClicked: false
  },
  {
    idx: 5,
    name: '알란토인',
    isClicked: false
  },
  {
    idx: 6,
    name: '리모넨',
    isClicked: false
  },
  {
    idx: 7,
    name: '베타인',
    isClicked: false
  },
  {
    idx: 8,
    name: '판테놀',
    isClicked: false
  },
  {
    idx: 9,
    name: '프로판다이올',
    isClicked: false
  },
  {
    idx: 10,
    name: '향료',
    isClicked: false
  },
  {
    idx: 11,
    name: '트로메타민',
    isClicked: false
  },
  {
    idx: 12,
    name: '잔탄검',
    isClicked: false
  },
  {
    idx: 13,
    name: '카보머',
    isClicked: false
  },
  {
    idx: 14,
    name: '펜틸렌글라이콜',
    isClicked: false
  },
  {
    idx: 15,
    name: '다이소듐이디티에이',
    isClicked: false
  },
  {
    idx: 16,
    name: '에틸헥실글리세린',
    isClicked: false
  },
  {
    idx: 17,
    name: '소듐하이알루로네이트',
    isClicked: false
  },
  {
    idx: 18,
    name: '나이아신아마이드',
    isClicked: false
  },
  {
    idx: 19,
    name: '하이드로제네이티드레시틴',
    isClicked: false
  }
]);

  const navigate = useNavigate();

  const showResult = async () => {
    navigate('/result');
  }

  const clickButton = (idx: number) => {
    dangerElementList[idx-1].isClicked = !(dangerElementList[idx-1].isClicked);
    setDangerElementList([...dangerElementList]);
  }
  return (
    <DangerElementWrap>
      {
        dangerElementList.map((item) => 
          <ButtonItemWrap style={{fontSize:'8px'}} clickedStatus={dangerElementList[item.idx-1].isClicked}>
            <motion.button
              key={item.idx}
              onClick={() => {clickButton(item.idx)}}
              className='buttonWrap'
              animate={{ scale: 2 }}
              transition={{ duration: 1 }}
              whileHover={{ scale: 2.2 }}
              whileTap={{ scale: 1.8 }}
            >{item.name}</motion.button>
          </ButtonItemWrap>
          
        )
      }
      <motion.button
        onClick={showResult}
        className='nextButtonWrap'
        animate={{ scale: 2 }}
        transition={{ duration: 1 }}
        whileHover={{ scale: 2.2 }}
        whileTap={{ scale: 1.8 }}
      >결과 확인하기</motion.button>

    </DangerElementWrap>
  )
}

export default DangerElement;

const DangerElementWrap = styled.div`
  display: grid; 
  grid-template-columns: repeat(7, 80px);
  row-gap: 40px;
  column-gap: 90px;

  .nextButtonWrap {
    background-color: #14C38E;
    border-radius: 10px;
    border: 1px solid #14C38E;
    color: white;
    font-weight: 600;
    font-size: 10px;
  }
`;
