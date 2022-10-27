import React, { useEffect, useState } from 'react'
import axios from 'axios'
import DeleteTable from './DeleteTable'

const V3 = (props) => {
    const [reg, setReg] = useState([])

    const [updateDate1, setUpdateDate1] = useState(new Date())
    const [updateDate2, setUpdateDate2] = useState(new Date())
    const [updateWho, setUpdateWho] = useState("")
    const [updateWhat, setUpdateWhat] = useState("")

    const [msg, setMsg] = useState("")
    useEffect(() => {
        axios.get(props.api).then(({ data }) => {
            console.log(data)
            if (Object.keys(data).length === 0) {
                setMsg("bad")
            } else {
                setMsg("good")
                console.log(`aaaaaaaaa:${data}`)
                console.log(`aaaaaaaaa:${data.who}`)
                setReg(data)
                console.log(`aaaaaaaaa:${reg}`)


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

    const handleUpdate = (e, id) => {
        e.preventDefault()
        const row = {}
        if (updateDate1.length > 0) {
            row['date_1'] = updateDate1
        }
        if (updateDate2.length > 0) {
            row['date_2'] = updateDate2

        }
        if (updateWho.length > 0) {
            row['who'] = updateWho

        }
        if (updateWhat.length > 0) {
            row['what'] = updateWhat

        }

        // const res = axios.put(`${props.api_update}/${id}`, { date_1: updateDate1, date_2: updateDate2, who: updateWho, what: updateWhat });
        const res = axios.put(`${props.api_update}/${id}`, row);
        // window.location.reload(false);


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

                    {reg.map(r =>


                        <tr key={r.registration_id}>
                            {/* <input type="text" value={r.registration_id}/> */}
                            {/* <td><input type="text" value={r.registration_id} /></td> */}

                            <td>{r.registration_id}</td>

                            <td><input type="date" defaultValue={r.date_1} onChange={e => setUpdateDate1(e.target.value)} /></td>
                            <td><input type="date" defaultValue={r.date_2} onChange={e => setUpdateDate2(e.target.value)} /></td>
                            <td><input type="text" defaultValue={r.who} onChange={e => setUpdateWho(e.target.value)} /></td>
                            <td><input type="text" defaultValue={r.what} onChange={e => setUpdateWhat(e.target.value)} /></td>
                            <button onClick={e => handleUpdate(e, r.registration_id)}>OK</button>


                            <button onClick={e => handleDelete(e, r.registration_id)}>DELETE</button>
                        </tr>
                    )}
                </table>
            </div>
            <p>{msg}</p>
            <DeleteTable api={props.api_delete_all} />
        </div>
    )
}

export default V3