import express from 'express'
import createError from 'http-errors'
import './db.js'
import routes from './routes.js'
const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use(routes)
app.use(async (req, res, next) => {
    next(new createError.NotFound())
})

app.use((err, req, res, next) => {
    res.status(err.status || 500)
    res.send({
        error: {
            status: err.status || 500,
            message: err.message,
        },
    })
})
const PORT = process.env.PORT || 4000
app.listen(PORT, () => { console.log(`🎯 running on ${PORT}`) })