import { body, validationResult } from 'express-validator'
import createError from "http-errors"
import { ad } from './models.js';
export const ValidationResult = (req, res, next) => {
    const result = validationResult(req);
    const hasErrors = !result.isEmpty();
    hasErrors ? res.send(result.mapped()) : next()
}
export const adValidation = [
    body("image", 'should be a valid Image Url')
        .trim()
        .notEmpty()
        .bail()
        .isString()
        .bail()
        .custom(async value => {
            if (await ad.findOne({ image: value }))
                throw new createError.Conflict(`Image ${value} is already been Used`)
        }),
    body("threshold_men_women_ratio", 'should be a valid Threshold men-woman ratio')
        .trim()
        .notEmpty()
        .bail()
        .isNumeric()
    , body("duration", 'should be a valid Duration')
        .trim()
        .notEmpty()
        .bail()
        .isNumeric(),
    body("threshhold_crowd_count", 'should be a valid Threshold crowd Count')
        .trim()
        .notEmpty()
        .bail()
        .isNumeric()
]