import express from 'express'
const app = express()

app.get("/", (req, res) => {

    const datime = new Date(new Date().toUTCString())
    const Total_crowd_count = Math.floor(Math.random() * (1500 - 5 + 1) + 5)
    const Men_women_Ratio = (Math.random()).toPrecision(2)

    const ifDisplayError = Math.floor(Math.random() * (7 - 2 + 1) + 2)
    const ifElectricityError = Math.floor(Math.random() * (7 - 2 + 1) + 2)
    const displayId = Math.floor(Math.random() * (500 - 100 + 1) + 100)
    const electricId = Math.floor(Math.random() * (500 - 100 + 1) + 100)

    if (ifDisplayError === 4 && ifElectricityError === 5) {
        res.send({
            timestamp: datime,
            Men_women_Ratio: Men_women_Ratio,
            Total_crowd_count: Total_crowd_count,
            diagnostics: {
                display: displayId,
                electricity: electricId
            }
        })
    }
    else if (ifElectricityError === 5) {
        res.send({
            timestamp: datime,
            Men_women_Ratio: Men_women_Ratio,
            Total_crowd_count: Total_crowd_count,
            diagnostics: {
                display: "OK",
                electricity: electricId
            }
        })
    }
    else if (ifDisplayError === 4) {
        res.send({
            timestamp: datime,
            Men_women_Ratio: Men_women_Ratio,
            Total_crowd_count: Total_crowd_count,
            diagnostics: {
                display: displayId,
                electricity: "OK"
            }
        })
    }
    else {
        res.send({
            timestamp: datime,
            Men_women_Ratio: Men_women_Ratio,
            Total_crowd_count: Total_crowd_count,
            diagnostics: {
                display: "OK",
                electricity: "OK"
            }
        })
    }

})


const PORT = process.env.PORT || 4000

app.listen(PORT, () => { console.log(`💎 running on ${PORT}`) })