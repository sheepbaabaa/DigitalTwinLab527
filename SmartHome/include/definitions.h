#ifndef __DEFINITIONS_H_
#define __DEFINITIONS_H_

// API status
#define API_STATUS_OK "ok"
#define API_STATUS_ASYNC "async"
#define API_STATUS_FAILED "failed"
#define API_STATUS_OK_CODE 0
#define API_STATUS_ASYNC_CODE 1
#define API_STATUS_FAILED_CODE -1
#define API_STATUS_INVALID_API_CODE -101
#define API_STATUS_INVALID_DATA_CODE -102
#define API_STATUS_DEVICE_NOT_FOUND_CODE -404

// Actions
#define API_SET_POWER_SWITCH "set_power_switch"
#define API_SET_AIR_CONDITIONER "set_air_conditioner"
#define API_SET_MONITOR_ELECTRICITY "set_monitor_electricity"

// Event types
#define EVENT_TYPE_MESSAGE "message"
#define EVENT_TYPE_NOTICE "notice"
#define EVENT_TYPE_META "meta"

// Notice event types
// TODO
#define NOTICE_EVENT_TYPE_RESERVED "reserved"
#define NOTICE_EVENT_TYPE_POWER_SWITCH_EVENT "power_switch"

// Meta event types
#define META_EVENT_TYPE_GATEWAY_UPDATE "gateway_update"
#define META_EVENT_TYPE_DEVICE_UPDATE "device_update"
#define META_EVENT_TYPE_HEARTBEAT "heartbeat"

#endif // __DEFINITIONS_H_