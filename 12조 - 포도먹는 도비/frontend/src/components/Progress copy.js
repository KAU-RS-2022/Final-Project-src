import ProgressBar from "progressbar.js"
import {useEffect} from "react"
import "./Progress.css"

function Progress() {

    useEffect(()=>{

        var circle = new ProgressBar.Line('#progress-bar', {
            color: '#ffffff',
            duration: 5000,
            easing: 'easeInOut'
        });
    
        circle.animate(1);
    })
    return (
    <div className="progress">
        <h1>당신의 취향에 맞는 와인 찾는 중 !</h1>
        <div className="progress-container">
        <div id="progress-bar">


        </div>
        </div>
        <div>
        <svg src="../pages/img/web3_check_icon.svg" class="check" width="100px" height="100px" border="" ></svg>
        <svg src="../pages/img/web3_arrow_icon.svg" class="arrow1" width="100px" height="100px" border="" ></svg>
        <svg src="../pages/img/web3_check_icon.svg" class="brain" width="100px" height="100px" border="" ></svg>
        <svg src="../pages/img/web3_arrow_icon.svg" class="arrow2" width="100px" height="100px" border="" ></svg>
        <svg src="../pages/img/web3_wine_icon.svg" class="wine" width="100px" height="100px" border="" ></svg>

        </div>
    </div>
    );
  }
  
  export default Progress;
  