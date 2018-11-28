import {Map} from 'immutable';

function getFilterIndex(state, itemId) {
  return state.get('filters').findIndex(
    (item) => item.get('id') === itemId
  );
}

function getMarkerIndex(state, itemId) {
  return state.get('markers').findIndex(
    (item) => item.get('title') === itemId
  );
}

function getFilters(state, filterIndex, inuse) {
  console.log(state.get('filters').get(filterIndex))
  return state.get('filters')
    .get(filterIndex)
    .set('inuse', inuse);
}

function updateMarker(state, markerIndex, mapOnVal) {
  return state.get('markers')
    .get(markerIndex)
    .update('mapOn', mapOn => mapOnVal);
}

function setState(state, newState) {
  return state.merge(newState);
}

function onMarkerClick(state, marker) {

  return state.merge(Map({
    'activeMarker': marker,
    'selectedTitle': marker.get('title'),
    'showingInfoWindow': true
  }))
}

function addMarker(state, marker) {
  let markers = state.get('gmapMarkers')
  let newMarkers = markers.push(marker)
  return state.update('gmapMarkers', oldmarkers => newMarkers)
}

function changeFilter(state, filter, inuse) {
  let filterIndex = getFilterIndex(state,filter)
  console.log("filterIndex",filterIndex)
  console.log("state",state)
  console.log("filter",filter)
  console.log("inuse",inuse)
  const updatedFilter = getFilters(state, filterIndex,inuse)
  console.log("update",updatedFilter)
  let updatedFilters = state.get('filters')
    console.log("update1", updatedFilters)
  updatedFilters = updatedFilters.set(filterIndex, updatedFilter)
  console.log("update2", updatedFilters)
  let active_filters = updatedFilters.filter(
    item => item.get('inuse') !== "N/A"
  )
  console.log("active", active_filters)

  let markers = state.get('markers')
  let updatedMarkers = markers
  markers.forEach(marker => {
    let markerIndex = getMarkerIndex(state, marker.get('title'))
    let mapOn = true
    active_filters.forEach(item => {
      if (marker.get('properties').get(item.get('id')) !== item.get('inuse')) {
        mapOn = false
      }
    })
    const updatedMarker = updateMarker(state, markerIndex, mapOn)
    updatedMarkers = updatedMarkers.set(markerIndex, updatedMarker)
  })

  return state.merge(Map({
    'filters': updatedFilters,
    'markers': updatedMarkers
  }))
}

export default function(state = Map(), action) {
  switch (action.type) {
    case 'SET_STATE':
      return setState(state, action.state);
    case 'CHANGE_FILTER':
        return changeFilter(state, action.filter, action.inuse);
    case 'MARKER_CLICK':
        return onMarkerClick(state, action.marker)
    case 'ADD_MARKER':
        return addMarker(state, action.marker)
    default:
      return state
  }
}
