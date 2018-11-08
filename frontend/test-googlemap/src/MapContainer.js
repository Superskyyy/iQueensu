import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-maps-react';
import React from 'react';

export class MapContainer extends React.Component {
    state = {
        activeMarker: {},
        selectedPlace: {},
        showingInfoWindow: false
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
        if (!this.props.loaded) return <div>Loading...</div>;
        const style = {
            width: '50%',
            marginBottom: 10,
            cssFloat: 'right',
            border:'1px solid black'

        }

        const style1 = {
            width:'40%',
            cssFloat:'left'
        }
        return (
            <div>
                <div>
                    <Map style={style1}
                        className="map"
                         google={this.props.google}
                         zoom={15}
                         initialCenter={{
                             lat: 44.2252795,
                             lng: -76.4973299
                         }}
                         onClick={this.onMapClicked}
                    >

                        <Marker
                            name="first house"
                            onClick={this.onMarkerClick}
                            position={{lat: 44.2237203, lng: -76.5018577}}
                        />

                        <Marker
                            name="second house"
                            onClick={this.onMarkerClick}
                            position={{lat: 44.2250563, lng: -76.5027347}}
                        />

                        <Marker
                            name="third house"
                            onClick={this.onMarkerClick}
                            position={{lat: 44.230562, lng: -76.498301}}
                        />

                        <InfoWindow
                            marker={this.state.activeMarker}
                            onClose={this.onInfoWindowClose}
                            visible={this.state.showingInfoWindow}>
                            <div>
                                <h1>{this.state.selectedPlace.name}</h1>
                            </div>
                        </InfoWindow>

                    </Map>
                </div>
                <div style={style}>
                    <h1>hahhahahahahah</h1>
                </div>
            </div>
        );
    }
}

export default GoogleApiWrapper({
    apiKey: ('AIzaSyApYnvaIs_OrTPauFoYfNpX149PhTJ_u44')
})(MapContainer)