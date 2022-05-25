import React from 'react'
import styled from '@emotion/styled';
import { Link } from 'react-router-dom';


const Main = () => {

  return (
    <RootWrap>
      <OpenDivWrap>
        <div className='openDivContent'>
          <div className='subtitle'>간단 설문을 통한 내게 맞는 화장품 찾기</div>
          <div className='title'>내 피부와 잘 맞는 화장품은?</div>
          <div className='imgWrap'>
            <img className='imgContent' src={require("../assets/cosmetic2.png")}></img>
            <span style={{width:'20px'}}></span>
            <img className='imgContent' src={require("../assets/cosmetic.png")}></img>
            <span style={{width:'20px'}}></span>
            <img className='imgContent' src={require("../assets/cosmetic3.png")}></img>
          </div>
          <Link to='/question'>
            <ButtonWrap>
              내게 맞는 화장품 찾으러 GO!
            </ButtonWrap>
          </Link>
        </div>
      </OpenDivWrap>
    </RootWrap>
  )
}

export default Main;

const RootWrap = styled.div`
  background-color:#439757;
`;

const OpenDivWrap = styled.div`
  width: 100vw;
  height: 100vh;
  padding: 180px;
  

  .openDivContent {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
  }
  .subtitle {
    font-size: 20px;
    margin-bottom: 20px;
  }

  .title {
    font-size: 32px;
    margin-bottom: 20px;
    font-weight: 600;
  }
  .imgWrap {
    display: flex;
  }
  .imgContent {
    width: 280px;
    height: 280px;
    border-radius: 20px;
    box-shadow: 3px 3px 3px;
  }
  
`;

const ButtonWrap = styled.div`
  font-size: 30px;
  height: 100px;
  background-color: white;
  border: 2px solid white;
  border-radius: 20px;
  color: rgb(0, 153, 79);
  font-weight: 700;
  padding: 20px;

  margin-top: 20px;

  &:hover {
    background-color: rgb(0, 0, 0, 0.5);
    color: white;
    transition: all 1s;
  }
`;