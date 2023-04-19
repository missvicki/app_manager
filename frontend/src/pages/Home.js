// import React from 'react';
import React from 'react';
import CustomPaginationActionsTable from '../components/PaginationTable.js';
import '../style_sheets/home.css';

const Home = () => {
  return (
    <div>
        <h1>
            Home
        </h1>
        <div className="Table">
            <CustomPaginationActionsTable />
        </div>
    </div>
  )
}

export default Home