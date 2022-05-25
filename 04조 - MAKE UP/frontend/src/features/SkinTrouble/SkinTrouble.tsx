
import styled from '@emotion/styled'
import React, { useEffect, useState } from 'react'
import { motion } from "framer-motion"
import { SetPageProps } from '../../pages/Question'
import { useRecoilState } from 'recoil'
import { selectedSkinTroubleListState } from './atom'

const SkinTrouble : React.FC<SetPageProps> = ({_setPage}) => {


  const [ selectedSkinTroubleList, setSelectedSkinTroubleList ] = useRecoilState(selectedSkinTroubleListState);
  
  const [ skinTroubleList, setSkinTroubleList ] = useState([
  {
    idx: 1,
    name: '트러블',
    isClicked: false
  },
  {
    idx: 2,
    name: '모공',
    isClicked: false
  },
  {
    idx: 3,
    name: '민감성',
    isClicked: false
  },
  {
    idx: 4,
    name: '잡티',
    isClicked: false
  },
  {
    idx: 5,
    name: '블랙헤드',
    isClicked: false
  },
  {
    idx: 6,
    name: '미백',
    isClicked: false
  },
  {
    idx: 7,
    name: '홍조',
    isClicked: false
  },
  {
    idx: 8,
    name: '탄력',
    isClicked: false
  },
  {
    idx: 9,
    name: '각질',
    isClicked: false
  },
  {
    idx: 10,
    name: '피지과다',
    isClicked: false
  },
  {
    idx: 11,
    name: '주름',
    isClicked: false
  },
  {
    idx: 12,
    name: '다크서클',
    isClicked: false
  },
  {
    idx: 13,
    name: '아토피',
    isClicked: false
  }
  ]);

  useEffect(() => {
    setSelectedSkinTroubleList([]);
  },[]);

  const clickButton = (idx: number) => {
    skinTroubleList[idx-1].isClicked = !(skinTroubleList[idx-1].isClicked);
    setSkinTroubleList([...skinTroubleList]);
  }

  const handleSkinTroubleClick = () => {
    let tempList : Array<string> = []
    skinTroubleList.map((item, idx) => {
      if(item.isClicked) {
        tempList.push(item.name)
      }
    })
    setSelectedSkinTroubleList(tempList);
    // 페이지 변경
    _setPage(4)
  }

  return (
    <SkinTroubleWrap>
      {
        skinTroubleList.map((item) => 
          <ButtonItemWrap clickedStatus={skinTroubleList[item.idx-1].isClicked}>
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
        onClick={handleSkinTroubleClick}
        className='nextButtonWrap'
        animate={{ scale: 2 }}
        transition={{ duration: 1 }}
        whileHover={{ scale: 2.2 }}
        whileTap={{ scale: 1.8 }}
      >다음</motion.button>
    </SkinTroubleWrap>
    
  )
}
export default SkinTrouble;

const SkinTroubleWrap = styled.div`
  display: grid;
  grid-template-rows: repeat(2);
  grid-template-columns: repeat(7, 70px);
  row-gap: 60px;
  column-gap: 60px;
  color: #439757;
  font-weight: 500;

  .buttonWrap {
    border-radius: 10px;
    background-color: white;
  }
  .nextButtonWrap {
    background-color: #B8F1B0;
    border-radius: 10px;
    border: 1px solid #B8F1B0;
    color: white;
    font-weight: 600;
  }
`;

export const ButtonItemWrap = styled.div`
  .buttonWrap {
    border-radius: 10px;
    background-color: ${({clickedStatus} : {clickedStatus:boolean}) => (clickedStatus ? '#36AE7C' : 'white') };
    color: ${({clickedStatus} : {clickedStatus:boolean}) => (clickedStatus ? 'white' : '#439757') };
    border: ${({clickedStatus} : {clickedStatus:boolean}) => (clickedStatus === true && 'none') };
  }
`;

