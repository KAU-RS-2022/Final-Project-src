import { useRef, useState } from "react";
import { useLocation } from "react-router-dom";
import Title from "../components/Title";
import "./WineInfo.css"

function WineInfo() {
    const location = useLocation()
    const data = location.state
    console.log(data)
    return (
      <div className="wine-info">
          <Title/>
          <div className="header-container">
          <div className="header">
          <h3>당신에게 딱 맞는 와인</h3>
          <img src="/wine_icon.svg"/> 
          </div>
          </div>
          <h1>{data.name}</h1>
          <img src={data.path}/>

          <div className="border-box"></div>
          <div className="info-container">
            <div className="column">
            <h6>type</h6>
            <h6>sweet</h6>
            <h6>acid</h6>
            <h6>body</h6>
            <h6>tannin</h6>

            </div>
            <div className="value">
                
            <h6>{data.type}</h6>
            <h6>{data.sweet}</h6>
            <h6>{data.acidity}</h6>
            <h6>{data.body}</h6>
            <h6>{data.tannin}</h6>
            </div>
          </div>
      </div>
    );
  }
  
  export default WineInfo;
