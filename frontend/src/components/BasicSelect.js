import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function BasicSelect(props) {
  const [maintainer, setMaintainer] = React.useState('');

  const handleChange = (event) => {
    setMaintainer(event.target.value);
  };

  return (
    <Box sx={{ paddingLeft: "10px", paddingBottom: "10px", width: "28.5%"}}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">{props.title}</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={maintainer}
          label={props.title}
          onChange={handleChange}
        >
        {props.arr.map((item) => {
            return <MenuItem key={item.id} value={item.name}>{item.name}</MenuItem>;
        })}
        </Select>
      </FormControl>
    </Box>
  );
}
