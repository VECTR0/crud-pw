import React, { useState } from 'react'
import axios from 'axios'


const V1 = (props) => {
    const [name, setName] = useState("")
    const [surname, setSurName] = useState("")
    const [problem, setProblem] = useState("")
    const [date2, setDate] = useState("")
    // const [date, setdate] = useState(new Date())

    const [msg, setMsg] = useState("")

    const handleButton = (e) => {
        e.preventDefault()
        setMsg("")

        if (date2!=="" && name.length !== 0 && surname.length !== 0 && problem.length !== 0) {
            var todayDate = new Date().toISOString().slice(0, 10);
            // var date = new Date(date2).toISOString().slice(0, 10);
            axios.post(props.api, {
                date_1: todayDate,
                date_2: new Date(date2).toISOString().slice(0, 10),
                who: `${name} ${surname}`,
                what: problem,
            }).then(res => {
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
                <input placeholder='Problem' type={"text"} onChange={e => setProblem(e.target.value)}></input>
                <input type="date" name="date" onChange={e => setDate(e.target.value)} />
                <button onClick={e => handleButton(e)}>Send</button>
            </form>
            <div>
                <p>{msg}</p>
            </div>
        </div>
    )
}

export default V1