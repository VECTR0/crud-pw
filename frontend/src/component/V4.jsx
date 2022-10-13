import React, { useState } from 'react'
import axios from 'axios'


const V4 = (props) => {
    const [regId, setRegId] = useState("")
    const [reg, setReg] = useState("")

    const [msg, setMsg] = useState("")

    const handleButton = (e) => {
        e.preventDefault()
        setReg("")
        if (regId.length !== 0) {
            axios.get(`${props.api}/${regId}`).then(({ data }) => {
                console.log(data)
                if (Object.keys(data).length === 0) {
                    setMsg("bad")
                } else {
                    setMsg("good")
                    const sep = "--------"
                    setReg(`${data.date_1}${sep}${data.date_2}${sep}${data.who}${sep}${data.what}`)
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
                <input placeholder='ID zgłoszenia' type={"text"} onChange={e => setRegId(e.target.value)}></input>

                <button onClick={e => handleButton(e)}>Send</button>

            </form>
            <div>
                <p>{msg}</p>
                <p>{reg}</p>
            </div>
        </div>
    )
}

export default V4