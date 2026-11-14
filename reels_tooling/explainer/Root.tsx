import React from 'react';
import {Composition} from 'remotion';
import {Overlay, OverlayProps} from './Overlay';
import {Explainer, ExplainerProps} from './Explainer';

// Una sola composición. La duración sale de los datos (props.json que genera
// scripts/alinear_subtitulos.py), así no hay que tocar este archivo por cada reel.
const ejemplo: OverlayProps = {
	durationInFrames: 150,
	cards: [{text: 'Tarjeta de\nejemplo', startFrame: 10, endFrame: 110, style: 'hook'}],
	subs: [{text: 'subtítulo de ejemplo', startFrame: 5, endFrame: 140}],
};

export const Root: React.FC = () => (
	<>
	<Composition id="Explainer" component={Explainer} durationInFrames={150} fps={30} width={1080} height={1920} defaultProps={{durationInFrames: 150, subs: []} as ExplainerProps} calculateMetadata={({props}) => ({durationInFrames: props.durationInFrames})} />
	<Composition
		id="Overlay"
		component={Overlay}
		durationInFrames={150}
		fps={30}
		width={1080}
		height={1920}
		defaultProps={ejemplo}
		calculateMetadata={({props}) => ({durationInFrames: props.durationInFrames})}
	/>
	</>
);
