import logo from './logo.svg';
import HomePage from './pages/HomePage';
import Survey from './pages/Survey';
import WineInfo from './pages/WineInfo';
import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <div className="App">
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/survey" element={<Survey />} />
        <Route path="/info" element={<WineInfo />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
