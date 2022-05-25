import styled from '@emotion/styled'
import { motion } from "framer-motion"
import React, { Dispatch, SetStateAction } from 'react'
import { useRecoilState } from 'recoil'
import { SetPageProps } from '../../pages/Question'
import { selectedSkinTypeState } from './atom'


const SkinType : React.FC<SetPageProps>= ({_setPage}) => {

  const [ skinTypeState, setSkinTypeState ] = useRecoilState(selectedSkinTypeState);


  const handleSkinTypeClick1 = () => {
    // 피부타입 : 건성
    setSkinTypeState('건성'); 

    // 페이지 변경
    _setPage(2)
  }
  const handleSkinTypeClick2 = () => {
    // 피부타입 : 지성 
    setSkinTypeState('지성'); 

    // 페이지 변경
    _setPage(2)
  }
  const handleSkinTypeClick3 = () => {
    // 피부타입 : 복합성 
    setSkinTypeState('복합성'); 

    // 페이지 변경
    _setPage(2)
  }

  return (
    <SkinTypeWrap>
      <div>
        <motion.button
          onClick={handleSkinTypeClick1}
          className='buttonWrap'
          animate={{ scale: 2 }}
          transition={{ duration: 1 }}
          whileHover={{ scale: 2.2 }}
          whileTap={{ scale: 1.5 }}
        >건성</motion.button>
      </div>
      <span style={{width:'120px'}}></span>
      <div>
        <motion.button
          onClick={handleSkinTypeClick2}
          className='buttonWrap'
          animate={{ scale: 2 }}
          transition={{ duration: 1 }}
          whileHover={{ scale: 2.2 }}
          whileTap={{ scale: 1.8 }}
        >지성</motion.button>
      </div>
      <span style={{width:'120px'}}></span>
      <div>
        <motion.button
          onClick={handleSkinTypeClick3}
          className='buttonWrap'
          animate={{ scale: 2 }}
          transition={{ duration: 1 }}
          whileHover={{ scale: 2.2 }}
          whileTap={{ scale: 1.8 }}
        >복합성</motion.button>
      </div>
    </SkinTypeWrap>
  )
}

export default SkinType;

const SkinTypeWrap = styled.div`
  display: flex;
  color: #439757;
  font-weight: 500;
  

  .buttonWrap {
    background-color: white;
    width: 100px;
    height: 100px;
    border-radius: 10px;
  }
  
`;
