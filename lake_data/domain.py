"""清点维度源事件和事实身份。"""
from .io import unique,integer

def summarize(v,root):
    unique(v['facts'],'fact_id');events=unique(v['events'],'event_id')
    for e in v['events']:
        if e['kind'] not in ('set','inactive','retract'):raise ValueError('事件类别未知')
        integer(e['revision'])
    return {'events':len(events),'facts':len(v['facts']),'natural_keys':len({e['key'] for e in v['events']})}
