import { Router } from 'express'
import { ad } from './models.js'
import { adValidation, ValidationResult } from './auth.js'
const routes = Router()

routes.post('/createad', adValidation, ValidationResult, async (req, res, next) => {
    try {
        const { image, duration, threshold_men_women_ratio, threshhold_crowd_count } = req.body
        const newAd = new ad({ image, duration, threshold_men_women_ratio, threshhold_crowd_count })
        const saved = await newAd.save()
        res.status(201)
        res.send({
            success: "Ok",
            saved
        })
    }
    catch (err) {
        next(err)
    }
})

export default routes