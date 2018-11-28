import React from 'react';
import {connect} from 'react-redux';
import {Jumbotron} from 'react-bootstrap';
import * as actionCreators from './action_creators';
import './App.css';
import CampFilterList from './CampFilterList';
import CampList from './CampList';
import CampMapContainer from './CampMapContainer';

export class CampFilterApp extends React.Component {

  render() {
    return (
      <div className="container">
        <br></br>
        <CampFilterList {...this.props}/>
        <br></br>
        <CampMapContainer {...this.props} />
        <br></br>
        <CampList {...this.props}/>

      </div>
  )};
}

function mapStateToProps(state) {
  return {
    filters: state.get('filters'),
    markers: state.get('markers'),
    showingInfoWindow: state.get('showingInfoWindow'),
    activeMarker: state.get('activeMarker'),
    selectedTitle: state.get('selectedTitle'),
    gmapMarkers: state.get('gmapMarkers')
  };
}


export const CampFilterAppContainer = connect(mapStateToProps,actionCreators)(CampFilterApp);
