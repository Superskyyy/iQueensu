import React, {Component} from 'react'
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import PostData from "./data";

export class MapContainer extends React.Component {

    state = {
        activeMarker: {},
        selectedPlace: {},
        showingInfoWindow: false,
    };

    onMarkerClick = (props, marker) =>
        this.setState({
            activeMarker: marker,
            selectedPlace: props,
            showingInfoWindow: true
        });
    onInfoWindowClose = () =>
        this.setState({
            activeMarker: null,
            showingInfoWindow: false
        });
    onMapClicked = () => {
        if (this.state.showingInfoWindow)
            this.setState({
                activeMarker: null,
                showingInfoWindow: false
            });
    };

    render() {
        return (
            <Map
                google={this.props.google}
                onClick={this.onMapClicked}
                initialCenter={{
                    lat: 44.2252795,
                    lng: -76.4973299
                }}
                zoom={15}>
                {PostData.map((dataDetail, id) => {
                    return <QMarker key={dataDetail.id}
                                    name={dataDetail.name}
                                    lat={dataDetail.lat}
                                    lng={dataDetail.lng}/>
                })}
                <InfoWindow
                    marker={this.state.activeMarker}
                    onClose={this.onInfoWindowClose}
                    visible={this.state.showingInfoWindow}>
                    <div>
                        <h1>{this.state.selectedPlace.name}</h1>
                    </div>
                </InfoWindow>
            </Map>
        )
    }
}

class QMarker extends React.Component {
    render() {
        return (
            <Marker key={this.props.id}
                    name={this.props.name}
                    lat={this.props.lat}
                    lng={this.props.lng}
                    onClick={this.onMarkerClick}/>
        )
    }
}

export default GoogleApiWrapper({
    apiKey: ("AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44")
})(MapContainer)