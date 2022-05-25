
import React from 'react';
import { BrowserRouter, Routes, Route, Link  } from 'react-router-dom';
import Main from './pages/Main';
import Question from './pages/Question';
import Result from './pages/Result';
import { Layout } from 'antd';
import { HomeOutlined, QuestionCircleOutlined } from '@ant-design/icons';
import styled from '@emotion/styled';
const { Header } = Layout;

function App() {

  return (
    <BrowserRouter>
      <Header style={{backgroundColor:'#55A666', color:'white', position:'absolute', left:'0', right:'0'}}>
        <HeaderContent >
          <Link to='/'>
            <span style={{fontSize:'16px', fontWeight:'600', color: 'white'}}>
              화장품 큐레이팅 서비스
            </span>
          </Link>
          <div style={{fontSize:'18px'}}>
            <Link to='/'>
              <HomeOutlined style={{marginRight:'16px', color:'white'}} />
            </Link>
            <QuestionCircleOutlined />
          </div>
        </HeaderContent>
      </Header>
      <Routes>
        <Route path='/' element={<Main/>} />
        <Route path='/question' element={<Question/>} />
        <Route path='/result' element={<Result/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

const HeaderContent = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;
