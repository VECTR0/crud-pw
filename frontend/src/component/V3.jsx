import React, { useEffect, useState } from 'react'
import axios from 'axios'

const V3 = (props) => {
    const [reg, setReg] = useState([])

    const [msg, setMsg] = useState("")
    useEffect(() => {
        axios.get(props.api).then(({ data }) => {
            console.log(data)
            if (Object.keys(data).length === 0) {
                setMsg("bad")
            } else {
                setMsg("good")
                setReg(data)
            }
        }).then(res => {
            console.log(res)
            if (res.status === 200) {
                setMsg("good")
            }
            else {
                setMsg("bad")
            }
            console.log(res.data);
        }).catch(err => {
            console.log(err);
        });
    }, [])

    const handleDelete = (e, id) => {
        e.preventDefault()
        axios.delete(`${props.api_delete}/${id}`).then(res => {
            if (res.status === 200) {
                window.location.reload(false);
            } else {
                console.log("aaaaaaa")
            }
        })
    }

    return (
        <div>
            <div>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>DATE_1</th>
                        <th>DATE_2</th>
                        <th>WHO</th>
                        <th>WHAT</th>
                    </tr>
                    {reg.map(r => <tr key={r.registration_id}>
                        <td>{r.registration_id}</td>
                        <td>{r.date_1}</td>
                        <td>{r.date_2}</td>
                        <td>{r.who}</td>
                        <td>{r.what}</td>
                        <button>OK</button>
                        <button onClick={e => handleDelete(e, r.registration_id)}>DELETE</button>
                    </tr>
                    )}
                </table>
            </div>
            <p>{msg}</p>
        </div>
    )
}

export default V3