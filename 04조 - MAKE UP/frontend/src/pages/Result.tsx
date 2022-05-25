import { AccountBookOutlined, UndoOutlined } from '@ant-design/icons';
import styled from '@emotion/styled';
import React, { useEffect, useState } from 'react'
import { Plane, Watch } from 'react-loader-spinner';
import { useNavigate } from 'react-router-dom';
import { useRecoilValue } from 'recoil';
import ResultItem, { ResultItemProps } from '../features/ResultItem/ResultItem';
import { selectedSkinTonState } from '../features/SkinTon/atom';
import { selectedSkinTroubleListState } from '../features/SkinTrouble/atom';
import { selectedSkinTypeState } from '../features/SkinType/atom';
import { customApiClient } from '../services/apiClient';

const Result = () => {

  const navigate = useNavigate();

  const skinType = useRecoilValue(selectedSkinTypeState);
  const skinTon = useRecoilValue(selectedSkinTonState);
  const skinTroubleList = useRecoilValue(selectedSkinTroubleListState);
  console.log(skinType);
  console.log(skinTon);
  console.log(skinTroubleList);

  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [cbfProduct1, setCbfProduct1] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cbfProduct2, setCbfProduct2] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cbfProduct3, setCbfProduct3] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cbfProduct4, setCbfProduct4] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cbfProduct5, setCbfProduct5] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});

  const [cfProduct1, setCfProduct1] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cfProduct2, setCfProduct2] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cfProduct3, setCfProduct3] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cfProduct4, setCfProduct4] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});
  const [cfProduct5, setCfProduct5] = useState<ResultItemProps>({productURL:'', imageURL:'', brand:'', price:0, productName:''});


  useEffect(() => {
    // API 호출
    getCFList();
    getCBFList();

    // 정상적으로 response를 받으면 flag값을 true로

  },[]);

  const getCFList = async () => {

    let url = `cf?skintype=${skinType}&skintone=${skinTon}`;
    skinTroubleList.map((item) => {
      url += `&skinworry=${item}`
    })
    console.log(url);
    
    const data = await customApiClient('get', url);

    //서버에러
    if (!data) {
      console.log('서버에러');
      return;
    } 

    console.log(data);

    setCfProduct1(data.CF['1']);
    setCfProduct2(data.CF['2']);
    setCfProduct3(data.CF['3']);
    setCfProduct4(data.CF['4']);
    setCfProduct5(data.CF['5']);

    data && setIsLoading(false);
  }
  const getCBFList = async () => {
    let url = `cbf?skintype=${skinType}&skintone=${skinTon}`;
    skinTroubleList.map((item) => {
      url += `&skinworry=${item}`
    })
    console.log(url);

    const data = await customApiClient('get', url);
    
    //서버에러
    if (!data) {
      console.log('서버에러');
      return;
    } 

    console.log(data);
    setCbfProduct1(data.CBF['1']);
    setCbfProduct2(data.CBF['2']);
    setCbfProduct3(data.CBF['3']);
    setCbfProduct4(data.CBF['4']);
    setCbfProduct5(data.CBF['5']);
    
    // data && setIsLoading(false);
  }


  return (
    <ResultWrap>
      {
        !isLoading ?
          <ContentWrap>
            <div className='headerWrap'>
              <img src='https://klinegroup.com/wp-content/uploads/naturals-and-cbd-blog-apr-2019.jpg'></img>
              <div className='headerTitle'>당신에게 딱 맞는 화장품은 바로~!</div>
            </div>
            <div className='resultWrap'>
              <ResultItem 
                productURL={cbfProduct1.productURL}
                imageURL={cbfProduct1.imageURL}
                brand={cbfProduct1.brand}
                price={cbfProduct1.price}
                productName={cbfProduct1.productName}/>
              <ResultItem 
                productURL={cbfProduct2.productURL}
                imageURL={cbfProduct2.imageURL}
                brand={cbfProduct2.brand}
                price={cbfProduct2.price}
                productName={cbfProduct2.productName}/>
              <ResultItem 
                productURL={cbfProduct3.productURL}
                imageURL={cbfProduct3.imageURL}
                brand={cbfProduct3.brand}
                price={cbfProduct3.price}
                productName={cbfProduct3.productName}/>
              <ResultItem 
                productURL={cbfProduct4.productURL}
                imageURL={cbfProduct4.imageURL}
                brand={cbfProduct4.brand}
                price={cbfProduct4.price}
                productName={cbfProduct4.productName}/>
              <ResultItem 
                productURL={cbfProduct5.productURL}
                imageURL={cbfProduct5.imageURL}
                brand={cbfProduct5.brand}
                price={cbfProduct5.price}
                productName={cbfProduct5.productName}/>
            </div>
            <div style={{fontSize:'32px', marginLeft:'100px'}}>당신과 비슷한 유저가 선호하는 제품은?</div>
            <div className='similarUserWrap'>
              {
                cfProduct1 && 
                <ResultItem
                productURL={cfProduct1.productURL}
                imageURL={cfProduct1.imageURL}
                brand={cfProduct1.brand}
                price={cfProduct1.price}
                productName={cfProduct1.productName} />
              }
              {
                cfProduct2 && 
                <ResultItem 
                productURL={cfProduct2.productURL}
                imageURL={cfProduct2.imageURL}
                brand={cfProduct2.brand}
                price={cfProduct2.price}
                productName={cfProduct2.productName}/>
              }
              {
                cfProduct3 && 
                <ResultItem 
                productURL={cfProduct2.productURL}
                imageURL={cfProduct2.imageURL}
                brand={cfProduct2.brand}
                price={cfProduct2.price}
                productName={cfProduct2.productName}/>
              }
              {
                cfProduct4 && 
                <ResultItem 
                productURL={cfProduct4.productURL}
                imageURL={cfProduct4.imageURL}
                brand={cfProduct4.brand}
                price={cfProduct4.price}
                productName={cfProduct4.productName}/>
              }
              {
                cfProduct5 && 
                <ResultItem 
                productURL={cfProduct5.productURL}
                imageURL={cfProduct5.imageURL}
                brand={cfProduct5.brand}
                price={cfProduct5.price}
                productName={cfProduct5.productName}/>
              }
            </div>
            <RetestButtonWrap onClick={() => navigate('/')}>
              <UndoOutlined style={{marginRight:'8px'}}  />
              <span>다시 추천받기</span>
            </RetestButtonWrap>
            <div style={{padding:'100px', backgroundColor:'rgb(240, 245, 237)', fontSize:'18px', fontWeight:'500', color:'#439757'}}>
              <AccountBookOutlined style={{marginRight:'4px'}} />
              TEAM MAKEUP
            </div>
            
          </ContentWrap>
          :
          <LoadingWrap>
            <Plane ariaLabel="loading-indicator" />
            <div>결과 분석 중입니다!</div>
          </LoadingWrap>
          
      }
    </ResultWrap>
  )
}

export default Result;


const ResultWrap = styled.div`
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
`;

const ContentWrap = styled.div`
  .headerWrap {
    position: relative;
    height: 550px;

    img {
      width: 100%;
    }
    .headerTitle {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translate(-50%);
      width: 640px;
      background-color: white;
      border: 0.5px solid rgba(0, 0, 0, 0.05);
      border-radius: 20px;
      box-shadow: rgb(0 0 0 / 4%) 0px 25px 35px;
      padding: 50px 0px;
      text-align: center;
      font-size: 32px;
      font-weight: 600;
      color: black;
    }
  }
  .resultWrap {
    margin: 100px ;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
  .similarUserWrap {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    margin: 30px 100px;

  }
  
`;

const LoadingWrap = styled.div`
  display: flex;
  padding: 100px;
  align-items: center;
  flex-direction: column;

  div {
    font-size: 16px;
    font-weight: 600;
  }
`;

const RetestButtonWrap = styled.div`
  font-size: 32px;
  color: rgb(100, 204, 128);
  width: 640px;
  height: 100px;
  border: 2px solid rgb(100, 204, 128);
  border-radius: 20px;

  display: flex;
  justify-content: center;
  align-items: center;
  margin: 80px auto;
  cursor: pointer;

  
`;