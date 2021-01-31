from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from bson.objectid import ObjectId
import requests
from db.ads import Ads
from db.ticket import Ticket
from depend import get_current_user
router = APIRouter()
adInstance = Ads()
tckt = Ticket()
URL = 'http://localhost:4000'
adDuration = 20
chargePerSec = 10


@router.get('/ad')
def get_ad_by_data(user=Depends(get_current_user)):
    try:
        adReq = requests.get(url=URL).json()
        allAds = adInstance.getAdsByGreaterThreshold(
            adReq['Men_women_Ratio'], adReq['Total_crowd_count'])
        max = []
        if not bool(allAds):
            max = adInstance.getMaxDurationAd()
        else:
            max = allAds[0]
            for ad in allAds:
                ad_duration = ad['duration']
                max_duration = max['duration']
                if ad_duration > max_duration:
                    max = ad
        if not adInstance.cutDurationOfads(max['_id'], adDuration, max['duration']):
            raise Exception('Internal server error')
        if not adInstance.updatePrice(max['_id'], adDuration*chargePerSec):
            raise Exception("Can't update price")
        diagnostics = adReq.get('diagnostics')
        if diagnostics:
            if diagnostics['display'] != 'OK':
                tckt.create_ticket({'display': diagnostics['display']})
            elif diagnostics['electricity'] != 'OK':
                tckt.create_ticket({'electricity': diagnostics['electricity']})
        return {'id': str(max['_id']), 'image': max['image'], 'duration': adDuration}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/ticket')
def get_ticket(id: str, user=Depends(get_current_user)):
    try:
        ticket = tckt.getTicketbyEmploee(id)
        if not ticket:
            raise Exception('Ticket not found')
        return {'jobs': ticket.get('job')}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
