import styled from '@emotion/styled';
import React from 'react'

export interface ResultItemProps {
  productURL: string,
  imageURL: string,
  brand: string,
  productName: string,
  price: number
}


const ResultItem : React.FC<ResultItemProps> = ({productURL, imageURL, brand, productName, price}) => {
  return (
    <a href={productURL} target='_blank'>
      <ResultItemWrap>
        <img src={imageURL}></img>
        <div className='brand'>{brand}</div>
        <div className='product'>{productName}</div>
        <div className='price'>{price}원</div>
      </ResultItemWrap>
    </a>
    
  )
}

export default ResultItem;

const ResultItemWrap = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
  img {
    border: 1px #F2F2F2 solid;
    border-radius: 5px;
    width: 312px;
    height: 312px;
  }
  .brand {
    font-size: 14px;
    font-weight: 600;
    margin-top: 12px;
    margin-bottom: 2px;
  }
  .product {
    font-size: 14px;
    margin-bottom: 8px;
  }
  .price {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 30px;
  }

  
`;