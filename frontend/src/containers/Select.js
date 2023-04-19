// import React from 'react';
import React, { useState, useEffect } from 'react';
import '../style_sheets/home.css';
import BasicSelect from '../components/BasicSelect';
import { Button } from '@mui/material';
import { useDispatch, useSelector } from "react-redux";
import TextField from "@mui/material/TextField";

import { fetch_technical_maintainers, fetch_functional_maintainers, fetch_dependencies } from '../redux/actions/Filter.actions';

const Select = () => {
  const dispatch = useDispatch();
  const { fetchTM } = fetch_technical_maintainers(dispatch);
  const { fetchFM } = fetch_functional_maintainers(dispatch);
  const { fetchDep } = fetch_dependencies(dispatch);

  const { techMaintainArr, } = useSelector(state => ({ ...state.filtersTMState }));
  const { funcMaintainArr, } = useSelector(state => ({ ...state.filtersFMState }));
  const { dependArr, } = useSelector(state => ({ ...state.filtersDepState }));

  useEffect(() => {
    async function fetchFilters() {
      await Promise.all([fetchTM()])
      await Promise.all([fetchFM()])
      await Promise.all([fetchDep()])
    }
    fetchFilters()
  }, [])

  return (
    <div>
      <div className="main">
        <div className="search">
          <TextField
            id="outlined-basic"
            variant="outlined"
            fullWidth
            label="Search"
          />
        </div>
      </div>

      <div
        style={{ display: "flex" }}>
        <BasicSelect arr={techMaintainArr} title="Technical Maintainer" />
        <BasicSelect arr={funcMaintainArr} title="Functional Maintainer" />
        <BasicSelect arr={dependArr} title="Dependencies" />
        <Button variant="contained" style={{
          marginLeft: "10px", marginBottom: "10px", width: "10%",
          backgroundColor: "#012169"
        }}>
          Apply
        </Button>
      </div>
    </div>
  )
}

export default Select