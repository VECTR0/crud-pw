import React, { useState } from 'react'
import axios from 'axios'


const V2 = (props) => {
    const [name, setName] = useState("")
    const [surname, setSurName] = useState("")
    const [reg, setReg] = useState([])
    const [msg, setMsg] = useState("")

    const handleButton = (e) => {
        e.preventDefault()
        setReg([])
        if (name.length !== 0 && surname.length !== 0) {
            axios.get(`${props.api}/${name} ${surname}`).then(({ data }) => {
                console.log(data)
                if (Object.keys(data).length === 0) {
                    setMsg("bad")
                } else {
                    setMsg("good")
                    setReg(data)
                    console.log("DUPA")
                    console.log(data)
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
        }
    }

    return (
        <div>
            <form>
                <input placeholder='Imię' type={"text"} onChange={e => setName(e.target.value)}></input>
                <input placeholder='Nazwisko' type={"text"} onChange={e => setSurName(e.target.value)}></input>
                <button onClick={e => handleButton(e)}>Send</button>
            </form>
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
                    </tr>
                    )}
                </table>
            </div>
        </div>
    )
}

export default V2