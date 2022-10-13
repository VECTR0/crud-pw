import axios from 'axios'
import React, { useState } from 'react'

const DeleteTable = (props) => {
  const [msg, setMsg] = useState("")
  const nieeeee = (e) => {
    e.preventDefault()
    setMsg("")
    axios.delete(props.api).then(res => {
      console.log(res);
      console.log(res.data);
      if (res.status === 200) {
        setMsg("Deleted")
      } else {
        setMsg("Not Deleted")
      }
    })
  }
  return (
    <div>
      <div><button onClick={e => nieeeee(e)}>Delete Whole Table</button></div>
      <div><p>{msg}</p></div>
    </div>
  )
}

export default DeleteTable