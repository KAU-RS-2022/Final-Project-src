import styled from '@emotion/styled';
import React from 'react'
import { motion } from "framer-motion"
import { SetPageProps } from '../../pages/Question';
import { useRecoilState } from 'recoil';
import { selectedSkinTonState } from './atom';

const SkinTon : React.FC<SetPageProps> = ({_setPage}) => {

  const [ skinTonState, setSkinTonState ] = useRecoilState(selectedSkinTonState);

  const handleSkinTonClick1 = () => {
    // 피부톤 : 웜톤
    setSkinTonState('웜톤');

    // 페이지 변경
    _setPage(3)
  }
  const handleSkinTonClick2 = () => {
    // 피부톤 : 쿨톤
    setSkinTonState('쿨톤');

    // 페이지 변경
    _setPage(3)
  }

  return (
    <SkinTonWrap>
      <div>
        <motion.button
          onClick={handleSkinTonClick1}
          className='buttonWrap'
          animate={{ scale: 2 }}
          transition={{ duration: 1 }}
          whileHover={{ scale: 2.2 }}
          whileTap={{ scale: 1.5 }}
        >웜톤</motion.button>
      </div>
      <span style={{width:'120px'}}></span>
      <div>
        <motion.button
          onClick={handleSkinTonClick2}
          className='buttonWrap'
          animate={{ scale: 2 }}
          transition={{ duration: 1 }}
          whileHover={{ scale: 2.2 }}
          whileTap={{ scale: 1.8 }}
        >쿨톤</motion.button>
      </div>
    </SkinTonWrap>
  )
}

export default SkinTon;

const SkinTonWrap = styled.div`
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
