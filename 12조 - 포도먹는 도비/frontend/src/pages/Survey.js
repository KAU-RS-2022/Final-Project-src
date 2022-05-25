import { useRef, useState } from "react";
import axios from "axios";
import Title from "../components/Title";
import Questions from "../components/Questions";
import Progress from "../components/Progress";
import "../components/Survey.scss"

function Survey() {
    const [data, setLoading] = useState(null)


    return (
      <div id="form-wrapper">
          <Title/> { data ?  <Progress data={data}/> :<Questions  updateData={setLoading}/> }

    {/* <ProgressBar/> */}
      </div>
    );
  }
  
  export default Survey;
