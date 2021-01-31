import mongoose from 'mongoose'
const Schema = mongoose.Schema

const ADSchema = new Schema({
    image: {
        type: String,
        required: true,
        lowercase: true,
        unique: true
    },
    threshold_men_women_ratio: {
        type: Number,
        required: true,
        max: 1,
        min: 0
    },
    duration: {
        type: Number,
        required: true,
        min: 15 * 60
    },
    threshhold_crowd_count: {
        type: Number,
        required: true,
        min: 4
    }
})

ADSchema.pre('save', async function (next) {
    try {
        if (this.isNew) {
            this.duration = Math.round(this.duration)
            this.threshhold_crowd_count = Math.round(this.threshhold_crowd_count)
        }
        next()
    } catch (error) {
        next(error)
    }
})
export const ad = mongoose.model('ad', ADSchema)