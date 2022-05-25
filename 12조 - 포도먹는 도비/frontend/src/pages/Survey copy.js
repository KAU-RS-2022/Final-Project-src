import { useRef, useState } from "react";
import axios from "axios";
import Title from "../components/Title";
import Questions from "../components/Questions";
import Progress from "../components/Progress";
import "../components/Survey.scss"

function Survey() {
    const [loading, setLoading] = useState(false)


    return (
      <div id="form-wrapper">
          <Title/> { loading ?  <Progress /> :<Questions callLoading={setLoading}/> }

    {/* <ProgressBar/> */}
      </div>
    );
  }
  
  export default Survey;
