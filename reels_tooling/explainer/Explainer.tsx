import React from 'react';
import {AbsoluteFill, Sequence, spring, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Icon} from './Icons';

export type SubSpec = {text: string; startFrame: number; endFrame: number};
export type ExplainerProps = {durationInFrames: number; subs: SubSpec[]; transparent?: boolean};

const FPS = 30;
const f = (s: number) => Math.round(s * FPS);
const FONT = 'Poppins, Arial, sans-serif';
const BLUE = '#4C8DFF';
const ORANGE = '#FF7A45';
const GREEN = '#35D07F';
const RED = '#FF4D5E';
const PANEL = '#141D38';
const BORDER = '#2C3A6B';

// Entrada con rebote a partir de un segundo dado (tiempo absoluto del video).
const usePop = (at: number, cfg = {damping: 11, stiffness: 170, mass: 0.6}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const p = spring({frame: frame - f(at), fps, config: cfg});
	return frame < f(at) ? 0 : p;
};

const Pop: React.FC<{at: number; children: React.ReactNode; style?: React.CSSProperties; from?: number; dy?: number; rot?: number}> = ({at, children, style, from = 0.4, dy = 30, rot = 0}) => {
	const p = usePop(at);
	return (
		<div style={{opacity: Math.min(1, p * 1.6), transform: `translateY(${(1 - p) * dy}px) scale(${from + (1 - from) * p}) rotate(${(1 - p) * rot}deg)`, filter: 'drop-shadow(0 6px 16px rgba(0,0,0,0.75))', ...style}}>{children}</div>
	);
};

// Se desvanece y sube al llegar el segundo `at`.
const useOut = (at: number) => {
	const frame = useCurrentFrame();
	return interpolate(frame, [f(at), f(at) + 9], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
};

const Chip: React.FC<{text: string; at: number}> = ({text, at}) => {
	const p = usePop(at, {damping: 12, stiffness: 200, mass: 0.5});
	return (
		<div style={{position: 'absolute', top: 250, left: 0, right: 0, display: 'flex', justifyContent: 'center', opacity: p, transform: `scale(${0.7 + 0.3 * p})`}}>
			<div style={{background: '#2E5AC8', color: '#fff', fontFamily: FONT, fontWeight: 700, fontStyle: 'italic', fontSize: 50, padding: '8px 34px', borderRadius: 12, boxShadow: '0 0 40px rgba(76,141,255,0.45)'}}>{text}</div>
		</div>
	);
};

const Card: React.FC<{icon: string; label: string; color?: string; w?: number; h?: number; iconSize?: number}> = ({icon, label, color = BLUE, w = 300, h = 250, iconSize = 110}) => (
	<div style={{width: w, height: h, borderRadius: 28, background: PANEL, border: `3px solid ${BORDER}`, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 14, boxShadow: `0 0 50px ${color}33`}}>
		<Icon name={icon} size={iconSize} color={color} />
		<div style={{fontFamily: FONT, fontWeight: 700, fontSize: 34, color: '#fff', textAlign: 'center', lineHeight: 1.1}}>{label}</div>
	</div>
);

const Stamp: React.FC<{text: string; at: number; color?: string; size?: number; rot?: number}> = ({text, at, color = BLUE, size = 92, rot = -7}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	const p = frame < f(at) ? 0 : spring({frame: frame - f(at), fps, config: {damping: 8, stiffness: 220, mass: 0.7}});
	return (
		<div style={{opacity: Math.min(1, p * 3), transform: `scale(${2.4 - 1.4 * p}) rotate(${rot}deg)`}}>
			<div style={{background: color, color: '#fff', fontFamily: FONT, fontWeight: 800, fontStyle: 'italic', fontSize: size, padding: '6px 40px', borderRadius: 14, border: '5px solid rgba(255,255,255,0.9)', boxShadow: `0 10px 50px ${color}99`, letterSpacing: 2}}>{text}</div>
		</div>
	);
};

const Scene: React.FC<{from: number; to: number; k?: number; children: React.ReactNode}> = ({from, to, k = 1.12, children}) => {
	const frame = useCurrentFrame();
	const a = f(from), b = f(to);
	const op = interpolate(frame, [a, a + 8, b - 8, b], [0, 1, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const ty = interpolate(frame, [a, a + 10], [26, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	if (frame < a || frame > b) return null;
	return <AbsoluteFill style={{opacity: op, transform: `translateY(${ty + (k > 1 ? 50 : 0)}px) scale(${k})`, transformOrigin: '50% 300px'}}>{children}</AbsoluteFill>;
};

const Abs: React.FC<{x?: number; y: number; children: React.ReactNode; w?: number}> = ({x = 540, y, children, w = 1000}) => (
	<div style={{position: 'absolute', left: x - w / 2, top: y, width: w, display: 'flex', justifyContent: 'center'}}>{children}</div>
);

// ---------- Escenas ----------
const S1: React.FC = () => {
	const out = useOut(5.6);
	return (
		<>
			<Chip text="Atención" at={0.5} />
			<Abs y={380}><Pop at={0.7}><div style={{width: 300, height: 300, borderRadius: 60, background: PANEL, border: `4px solid ${BORDER}`, display: 'flex', alignItems: 'center', justifyContent: 'center'}}><Icon name="briefcase" size={190} color="#fff" /></div></Pop></Abs>
			<Abs x={690} y={350}><Pop at={1.9}><div style={{background: BLUE, borderRadius: 40, padding: 22, boxShadow: `0 0 50px ${BLUE}`}}><Icon name="shield" size={110} color="#fff" /></div></Pop></Abs>
			<Abs y={720}><Pop at={2.0}><div style={{fontFamily: FONT, fontWeight: 800, fontSize: 66, color: '#fff', textAlign: 'center'}}>CARGO DE <span style={{color: BLUE}}>CONFIANZA</span></div></Pop></Abs>
			<Abs y={880}>
				<div style={{display: 'flex', alignItems: 'center', gap: 50, opacity: 1 - out * 0}}>
					<Pop at={2.7}><Icon name="user" size={150} color="#fff" /></Pop>
					<Pop at={3.7}><RotatingArrow /></Pop>
					<Pop at={3.7}><div style={{fontFamily: FONT, fontWeight: 800, fontSize: 52, color: '#fff'}}>REPOSICIÓN</div></Pop>
				</div>
			</Abs>
			<Abs x={430} y={870}><Pop at={5.1}><Icon name="x" size={190} color={RED} stroke={2.6} /></Pop></Abs>
		</>
	);
};

const RotatingArrow: React.FC = () => {
	const frame = useCurrentFrame();
	const rot = interpolate(frame, [f(3.7), f(4.5)], [-360, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	return <div style={{transform: `rotate(${rot}deg)`}}><Icon name="refresh" size={140} color={GREEN} /></div>;
};

const S2: React.FC = () => {
	const frame = useCurrentFrame();
	const fall = interpolate(frame, [f(14.5), f(15.3)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const join = interpolate(frame, [f(11.8), f(12.3)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const gap = 360 - 60 * join;
	return (
		<>
			<Chip text="La Corte Suprema" at={5.9} />
			<Abs y={360}><Pop at={5.9} rot={-35}><Icon name="gavel" size={230} color={ORANGE} /></Pop></Abs>
			<Abs y={640}><Pop at={7.1}><div style={{display: 'flex', alignItems: 'center', gap: 16, background: PANEL, border: `3px solid ${BORDER}`, borderRadius: 40, padding: '14px 34px'}}><Icon name="news" size={56} color="#fff" /><span style={{fontFamily: FONT, fontWeight: 700, fontSize: 40, color: '#fff'}}>Fuente: Gestión</span></div></Pop></Abs>
			<Abs y={800}><Stamp text="FUNCIONES MIXTAS" at={9.5} size={64} rot={-4} /></Abs>
			<div style={{position: 'absolute', left: 0, right: 0, top: 950, display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
				<div style={{display: 'flex', alignItems: 'center', width: gap + 300, justifyContent: 'space-between', position: 'relative', opacity: 1 - interpolate(frame, [f(13.1), f(13.4)], [0, 0.85], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}}>
					<Pop at={10.4}><div style={{transform: `translateY(${fall * 260}px) rotate(${fall * 14}deg)`, opacity: 1 - fall}}><Card icon="shield" label="DE CONFIANZA" w={280} h={230} /></div></Pop>
					<Pop at={11.8} style={{position: 'absolute', left: '50%', top: '50%', marginLeft: -40, marginTop: -40}}><Icon name="plus" size={80} color="#fff" /></Pop>
					<Pop at={11.2}><Card icon="clipboard" label="ORDINARIAS" color={ORANGE} w={280} h={230} /></Pop>
				</div>
			</div>
			<Abs y={1040}><Stamp text="SIN REPOSICIÓN" at={13.2} color={RED} size={84} rot={6} /></Abs>
		</>
	);
};

const S3: React.FC = () => {
	const frame = useCurrentFrame();
	const line = interpolate(frame, [f(21.0), f(21.7)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
	const tl = 1 - useOut(24.0);
	return (
		<>
			<Chip text="El matiz" at={16.3} />
			<Abs y={380}><Pop at={16.4}><Icon name="alert" size={190} color="#FFC83D" /></Pop></Abs>
			<div style={{position: 'absolute', left: 0, top: 640, width: 1080, opacity: tl, transform: `translateY(${(1 - tl) * -30}px)`}}>
				<Abs x={260} y={0} w={420}><Pop at={19.4}><Card icon="clipboard" label={'1º PUESTO\nORDINARIO'} color={ORANGE} w={340} h={260} /></Pop></Abs>
				<div style={{position: 'absolute', left: 430, top: 130, width: 220 * line, height: 8, background: BLUE, borderRadius: 4, boxShadow: `0 0 20px ${BLUE}`}} />
				<Abs x={820} y={0} w={420}><Pop at={21.7}><Card icon="shield" label={'LUEGO\nCONFIANZA'} w={340} h={260} /></Pop></Abs>
				<Abs y={330}><Pop at={23.4}><div style={{display: 'flex', alignItems: 'center', gap: 20, background: GREEN, borderRadius: 24, padding: '18px 40px', boxShadow: `0 0 60px ${GREEN}88`}}><Icon name="check" size={80} color="#0B1220" stroke={3} /><span style={{fontFamily: FONT, fontWeight: 800, fontSize: 58, color: '#0B1220'}}>MÁS PROTECCIÓN</span></div></Pop></Abs>
			</div>
			<Abs y={380}><Pop at={24.2}><div style={{display: 'flex', alignItems: 'center', gap: 28, background: PANEL, border: `3px solid ${BORDER}`, borderRadius: 40, padding: '26px 44px'}}><div style={{background: BLUE, borderRadius: 100, padding: 22}}><Icon name="user" size={100} color="#fff" /></div><div><div style={{fontFamily: FONT, fontWeight: 800, fontSize: 56, color: '#fff'}}>Katy Noriega</div><div style={{fontFamily: FONT, fontWeight: 600, fontSize: 40, color: BLUE}}>Especialista · PPU</div></div></div></Pop></Abs>
			<Abs y={720}><Pop at={26.0} rot={-20}><Icon name="scale" size={220} color="#fff" /></Pop></Abs>
			<Abs y={980}><Pop at={26.9}><div style={{fontFamily: FONT, fontWeight: 800, fontSize: 56, color: '#fff', textAlign: 'center'}}>Criterio para <span style={{color: BLUE}}>distinguir</span><br />ambos casos</div></Pop></Abs>
		</>
	);
};

const Row: React.FC<{icon: string; text: string; at: number}> = ({icon, text, at}) => (
	<Pop at={at} dy={20}>
		<div style={{display: 'flex', alignItems: 'center', gap: 22, width: 860, padding: '10px 0'}}>
			<Icon name={icon} size={52} color={BLUE} />
			<div style={{fontFamily: FONT, fontWeight: 600, fontSize: 40, color: '#fff', flex: 1}}>{text}</div>
			<Icon name="check" size={48} color={GREEN} stroke={3} />
		</div>
	</Pop>
);

const Panel: React.FC<{at: number; icon: string; title: string; color: string; y: number; children: React.ReactNode}> = ({at, icon, title, color, y, children}) => (
	<Abs y={y} w={960}>
		<Pop at={at} dy={40} style={{width: 940}}>
			<div style={{background: PANEL, border: `3px solid ${BORDER}`, borderRadius: 34, padding: '22px 40px 20px', boxShadow: `0 0 60px ${color}22`, width: 940}}>
				<div style={{display: 'flex', alignItems: 'center', gap: 20, marginBottom: 6}}>
					<div style={{background: color, borderRadius: 18, padding: 12}}><Icon name={icon} size={60} color="#fff" /></div>
					<div style={{fontFamily: FONT, fontWeight: 800, fontSize: 52, color: '#fff'}}>{title}</div>
				</div>
				<div style={{minHeight: 290}}>{children}</div>
			</div>
		</Pop>
	</Abs>
);

const S4: React.FC = () => (
	<>
		<Chip text="Qué hacer" at={28.7} />
		<Panel at={28.8} icon="building" title="EMPLEADOR" color={BLUE} y={340}>
			<Row icon="calendar" text="Fecha del cambio de funciones" at={30.4} />
			<Row icon="file" text="Cómo lo documentaste" at={31.3} />
			<Row icon="clipboard" text="Funciones de cada trabajador" at={33.0} />
		</Panel>
		<Panel at={35.0} icon="user" title="TRABAJADOR" color={ORANGE} y={800}>
			<Row icon="calendar" text="¿Desde cuándo tuviste confianza?" at={36.3} />
			<Row icon="clipboard" text="¿Qué funciones cumplías?" at={37.6} />
			<Row icon="scale" text="¿Tienes derecho a reposición?" at={39.5} />
		</Panel>
	</>
);

const S5: React.FC = () => {
	const frame = useCurrentFrame();
	const pulse = 1 + 0.05 * Math.sin((frame - f(42.2)) / 4);
	return (
		<>
			<Abs y={620}><Pop at={42.2}><div style={{display: 'flex', alignItems: 'center', gap: 24, background: BLUE, borderRadius: 100, padding: '28px 70px', boxShadow: `0 0 80px ${BLUE}`, transform: `scale(${pulse})`}}><Icon name="plus" size={90} color="#fff" stroke={3} /><span style={{fontFamily: FONT, fontWeight: 800, fontSize: 100, color: '#fff'}}>Sígueme</span></div></Pop></Abs>
			<Abs y={900}><Pop at={43.2}><div style={{fontFamily: FONT, fontWeight: 600, fontSize: 44, color: '#fff', textAlign: 'center'}}>Víctor Ventura · <span style={{color: BLUE}}>Ventura Legal</span></div></Pop></Abs>
		</>
	);
};

// ---------- Subtítulos con palabra clave ----------
const KEY = new Set(['confianza', 'reposición', 'reposicion', 'repuesto', 'mixtas', 'suprema', 'ordinario', 'ordinarias', 'protección', 'empleador', 'trabajador', 'derecho', 'documentaste', 'puesto', 'gestión', 'criterio']);
const norm = (w: string) => w.toLowerCase().replace(/[^a-záéíóúñ]/g, '');

const Sub: React.FC<{sub: SubSpec; tr?: boolean}> = ({sub, tr}) => {
	const frame = useCurrentFrame();
	const {fps} = useVideoConfig();
	if (frame < sub.startFrame || frame >= sub.endFrame) return null;
	const p = spring({frame: frame - sub.startFrame, fps, config: {damping: 15, stiffness: 260, mass: 0.4}});
	return (
		<div style={{position: 'absolute', left: 0, right: 0, top: 1330, height: 200, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '0 80px'}}>
			<div style={{transform: `scale(${0.88 + 0.12 * p})`, opacity: Math.min(1, 0.4 + p), fontFamily: FONT, fontWeight: 700, fontSize: sub.text.length > 26 ? 62 : 70, textAlign: 'center', lineHeight: 1.12, color: '#fff', maxWidth: 920, ...(tr ? {WebkitTextStroke: '10px rgba(0,0,0,0.92)', paintOrder: 'stroke fill', textShadow: '0 4px 14px rgba(0,0,0,0.8)'} : {})}}>
				{sub.text.split(' ').map((w, i) => (
					<span key={i} style={{color: KEY.has(norm(w)) ? BLUE : '#fff'}}>{w}{' '}</span>
				))}
			</div>
		</div>
	);
};

export const Explainer: React.FC<ExplainerProps> = ({subs, transparent}) => (
	<AbsoluteFill style={{background: transparent ? 'transparent' : 'radial-gradient(ellipse at 50% 40%, #16224A 0%, #0B1220 70%)', overflow: 'hidden'}}>
		{!transparent && <AbsoluteFill style={{backgroundImage: 'linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)', backgroundSize: '90px 90px'}} />}
		<Scene from={0.4} to={5.9}><S1 /></Scene>
		<Scene from={5.8} to={16.4}><S2 /></Scene>
		<Scene from={16.3} to={28.8}><S3 /></Scene>
		<Scene from={28.7} to={42.3} k={1}><S4 /></Scene>
		<Scene from={42.2} to={45.44}><S5 /></Scene>
		{subs.map((s, i) => (<Sub key={i} sub={s} tr={transparent} />))}
	</AbsoluteFill>
);
