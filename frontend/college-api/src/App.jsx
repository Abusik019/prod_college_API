import "./App.css";
import { Routes, Route } from "react-router-dom";
import Main from "./pages/Main";
import Login from './pages/Login';
import Structure from './pages/Structure/index';


function App() {
    return (
        <Routes>
            <Route path="*" element={<Main />} />
            <Route path='/login' element={<Login />}/>
            <Route path='/structure' element={<Structure />}/>
        </Routes>
    );
}

export default App;
