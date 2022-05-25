import Title from "../components/Title";
import "../components/HomePage.scss"

import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

function HomePage() {
  return (
    <div className="home-page">

      <Title/>
      {/* <div className="start-survey" style="position: relative;"> */}
      <div className="start-survey" >
      {/* <svg src="./img/web1_img1.jpg" class="circle" width="100px" height="100px" border="" ></svg> */}
        
        {/* <div style="position: absolute; top: 50px; left: 50px;"> */}
      <Link to="survey" className="start-link">
        <svg src="./img/web1_1.svg" class="wine_icon" width="100px" height="100px" border=""></svg>
        </Link>
        {/* </div> */}
      
      </div>
      <div className="help-text">
        <span>와인 잔을 클릭하고 간단한 5가지 질문에 답해주세요!</span><br/>
        <span>취향에 맞는 와인을 추천해드립니다</span>
      </div>
    </div>
  );
}

export default HomePage;
