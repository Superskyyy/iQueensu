import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import {createStore} from 'redux';
import reducer from './reducer'
import {CampFilterAppContainer} from './CampFilterApp';
import './index.css';
import postdata from './postdata.json';


const store = createStore(reducer)

// convert json into dict for use by the React components
// add mapOn variable to indicate if the marker should be visible
// by default, set mapOn to false, filtering will indicate if it should be true
function get_campgrounds(features) {
  let campgrounds = []
  features.forEach(feature => {
    campgrounds.push({
      'title' : feature['properties']['title'],
      'description' : feature['properties']['description'],
      'position' : [feature['geometry']['coordinates'][1],
      feature['geometry']['coordinates'][0]],
      'properties': feature['properties'],
      'image': feature['properties']['image'],
      'url': feature['properties']['url'],
      'mapOn': true

    })
  });
  return campgrounds
}

let features = postdata


set_state(get_campgrounds(features))

function set_state(campgrounds) {
  store.dispatch ({
  type: 'SET_STATE',
  state: {
    filters: [
      {id: 'bedroom', inuse: "N/A", options: ["N/A", "1", "2", "3", "4", "5+"]},
      {id: 'washroom', inuse: "N/A", options: ["N/A", "1", "2", "3", "4+"]},
      {id: 'type', inuse: "N/A", options: ["N/A", "house", "apartment"]}
    ],
    markers: campgrounds,
    gmapMarkers: [],
    showingInfoWindow: "false",
    activeMarker: null,
    selectedTitle: ""
  }
 })
}

ReactDOM.render(
  <Provider store={store}>
  <CampFilterAppContainer />
</Provider>,
  document.getElementById('root')
);
