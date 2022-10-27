import React, { } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import V1 from './component/V1';
import V2 from './component/V2';
import V3 from './component/V3';
import V4 from './component/V4';
import DeleteTable from './component/DeleteTable';
require('dotenv').config();

const App = () => {
  const API_REG_GET = process.env.REACT_APP_API_REG_GET
  const API_REG_GET_ID = process.env.REACT_APP_API_REG_GET_ID
  const API_REG_GET_BY_NAME = process.env.REACT_APP_API_REG_GET_BY_NAME
  const API_REG_ADD = process.env.REACT_APP_API_REG_ADD
  const API_REG_UPDATE_ID = process.env.REACT_APP_API_REG_UPDATE_ID
  const API_REG_DELETE_ID = process.env.REACT_APP_API_REG_DELETE_ID
  const API_REG_DELETE_ALL = process.env.REACT_APP_API_REG_DELETE_ALL


  return (
    <Router>
      <Routes>
        <Route exact path="/del" element={<DeleteTable api={API_REG_DELETE_ALL} />} />

        <Route exact path="/v1" element={<V1 api={API_REG_ADD} />} />
        <Route exact path="/v2" element={<V2 api={API_REG_GET_BY_NAME} />} />
        <Route exact path="/v3" element={<V3 api={API_REG_GET} api_delete={API_REG_DELETE_ID} api_delete_all={API_REG_DELETE_ALL} api_update={API_REG_UPDATE_ID} />} />
        <Route exact path="/v4" element={<V4 api={API_REG_GET}  />} />
        <Route path="*" element={<p>404</p>} />
      </Routes>

    </Router>
  );
}

export default App