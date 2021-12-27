--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: contracts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contracts (
    id integer NOT NULL,
    contract_name character varying(50) NOT NULL,
    customer_name character varying(50) NOT NULL,
    open_reqs integer
);


ALTER TABLE public.contracts OWNER TO postgres;

--
-- Name: contracts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contracts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contracts_id_seq OWNER TO postgres;

--
-- Name: contracts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contracts_id_seq OWNED BY public.contracts.id;


--
-- Name: employee_to_contracts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee_to_contracts (
    employee_id integer NOT NULL,
    contract_id integer NOT NULL,
    labor_id integer NOT NULL
);


ALTER TABLE public.employee_to_contracts OWNER TO postgres;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    id integer NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    email_address character varying(50) NOT NULL,
    labor_id integer NOT NULL,
    contract_id integer NOT NULL
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- Name: employees_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employees_id_seq OWNER TO postgres;

--
-- Name: employees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;


--
-- Name: labor_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.labor_categories (
    id integer NOT NULL,
    labor_code character varying(5) NOT NULL,
    labor_category character varying(100) NOT NULL,
    salary numeric(10,2) NOT NULL
);


ALTER TABLE public.labor_categories OWNER TO postgres;

--
-- Name: labor_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.labor_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.labor_categories_id_seq OWNER TO postgres;

--
-- Name: labor_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.labor_categories_id_seq OWNED BY public.labor_categories.id;


--
-- Name: contracts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts ALTER COLUMN id SET DEFAULT nextval('public.contracts_id_seq'::regclass);


--
-- Name: employees id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);


--
-- Name: labor_categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.labor_categories ALTER COLUMN id SET DEFAULT nextval('public.labor_categories_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
2106f55289b9
\.


--
-- Data for Name: contracts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contracts (id, contract_name, customer_name, open_reqs) FROM stdin;
1	CRAFTYPANDA	Baltimore Gas & Electric	3
2	SUNRISE	Department of Energy	20
3	CODEELF	Department of Defense	0
4	ARMORBYTE	Montgomery County Police Department	5
5	STUDYHALL	University of Maryland	0
6	JUNEBEAR	Verizon Wireless	10
\.


--
-- Data for Name: employee_to_contracts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee_to_contracts (employee_id, contract_id, labor_id) FROM stdin;
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employees (id, first_name, last_name, email_address, labor_id, contract_id) FROM stdin;
2	Joshua	Page	joshua.page96@infotech.com	11	3
3	Jessica	Doyle	jessica.doyle96@infotech.com	10	5
4	Jenna	Sanders	jenna.sanders27@infotech.com	4	4
5	Alexandra	Johnson	alexandra.johnson5@infotech.com	8	3
6	Rebecca	Evans	rebecca.evans98@infotech.com	12	5
7	Linda	Manning	linda.manning26@infotech.com	1	2
8	Nicholas	King	nicholas.king26@infotech.com	12	2
9	Jennifer	Ramos	jennifer.ramos32@infotech.com	9	3
10	Michelle	Harrison	michelle.harrison2@infotech.com	9	1
11	Gregory	Abbott	gregory.abbott88@infotech.com	4	4
12	Carla	Ford	carla.ford61@infotech.com	5	5
13	Jonathan	Arnold	jonathan.arnold98@infotech.com	8	2
14	Ian	Miller	ian.miller96@infotech.com	12	4
15	Susan	Jones	susan.jones9@infotech.com	3	4
16	Ashley	Joyce	ashley.joyce55@infotech.com	4	3
17	John	Montgomery	john.montgomery79@infotech.com	1	4
18	Becky	Brewer	becky.brewer66@infotech.com	6	1
19	Christopher	Dunn	christopher.dunn16@infotech.com	5	4
20	Leslie	Clark	leslie.clark36@infotech.com	1	1
21	Kayla	Barnett	kayla.barnett72@infotech.com	1	2
22	Anna	Hooper	anna.hooper70@infotech.com	10	4
23	Melissa	Ray	melissa.ray66@infotech.com	8	3
24	James	Clements	james.clements24@infotech.com	3	5
25	Shane	Sims	shane.sims63@infotech.com	9	3
26	Kristen	Robinson	kristen.robinson80@infotech.com	1	1
27	Amanda	Lopez	amanda.lopez23@infotech.com	11	4
28	William	Lewis	william.lewis28@infotech.com	12	1
29	Francis	Hill	francis.hill38@infotech.com	12	4
30	Steven	Wells	steven.wells7@infotech.com	11	4
31	Tracy	Good	tracy.good92@infotech.com	7	4
32	Amy	Potts	amy.potts10@infotech.com	12	4
33	Henry	Lindsey	henry.lindsey41@infotech.com	1	1
34	Stephanie	Davis	stephanie.davis96@infotech.com	4	1
35	Hannah	Sweeney	hannah.sweeney42@infotech.com	9	1
36	Mary	Glenn	mary.glenn60@infotech.com	7	2
37	Scott	Young	scott.young63@infotech.com	10	2
38	Nicole	Thompson	nicole.thompson12@infotech.com	1	5
39	Michael	Washington	michael.washington43@infotech.com	8	3
40	Tony	Ramirez	tony.ramirez94@infotech.com	5	1
41	Charles	Ferguson	charles.ferguson68@infotech.com	9	4
42	Andrew	George	andrew.george95@infotech.com	1	3
43	Jose	Morales	jose.morales41@infotech.com	4	4
44	Carl	Lamb	carl.lamb65@infotech.com	4	3
45	Bobby	Yoder	bobby.yoder92@infotech.com	10	1
46	Sandra	Fowler	sandra.fowler34@infotech.com	5	2
47	Cheryl	Beasley	cheryl.beasley56@infotech.com	8	5
48	Victor	Weaver	victor.weaver56@infotech.com	7	1
49	Ellen	Monroe	ellen.monroe46@infotech.com	1	3
50	David	Payne	david.payne39@infotech.com	4	3
51	Katelyn	Cruz	katelyn.cruz66@infotech.com	8	2
52	Autumn	Turner	autumn.turner39@infotech.com	3	2
53	Jon	Irwin	jon.irwin60@infotech.com	11	1
54	Lisa	Combs	lisa.combs57@infotech.com	3	2
55	Raymond	Hammond	raymond.hammond26@infotech.com	3	3
56	Sara	Spencer	sara.spencer86@infotech.com	9	1
57	Brian	Goodman	brian.goodman74@infotech.com	5	3
58	Craig	Rhodes	craig.rhodes71@infotech.com	8	2
59	Lucas	Brown	lucas.brown69@infotech.com	9	1
60	Laura	Potter	laura.potter28@infotech.com	11	4
61	Cynthia	Haney	cynthia.haney46@infotech.com	12	5
62	Benjamin	Bell	benjamin.bell34@infotech.com	3	1
63	Thomas	Mcdonald	thomas.mcdonald63@infotech.com	1	1
64	Dylan	Murphy	dylan.murphy87@infotech.com	6	4
65	Ann	Salinas	ann.salinas38@infotech.com	11	3
66	Deanna	Knox	deanna.knox5@infotech.com	10	2
67	Nathaniel	Nolan	nathaniel.nolan8@infotech.com	10	3
68	Stacy	Rocha	stacy.rocha13@infotech.com	10	4
69	Adam	Morgan	adam.morgan71@infotech.com	1	4
70	Alicia	Hicks	alicia.hicks18@infotech.com	7	3
71	Patrick	Maldonado	patrick.maldonado41@infotech.com	4	1
72	Erica	Saunders	erica.saunders45@infotech.com	2	4
73	Chelsea	Smith	chelsea.smith69@infotech.com	1	4
74	Jacob	Logan	jacob.logan72@infotech.com	9	3
75	Kevin	Daniel	kevin.daniel86@infotech.com	6	5
76	Frederick	Molina	frederick.molina37@infotech.com	6	3
77	Jason	Martinez	jason.martinez23@infotech.com	9	1
78	Timothy	Curry	timothy.curry20@infotech.com	1	4
79	Katherine	Watson	katherine.watson48@infotech.com	9	4
80	Justin	Anderson	justin.anderson14@infotech.com	2	3
81	Dennis	Caldwell	dennis.caldwell89@infotech.com	2	2
82	Megan	Porter	megan.porter62@infotech.com	10	5
83	Kim	Stewart	kim.stewart44@infotech.com	6	1
84	Andrea	Daniels	andrea.daniels79@infotech.com	4	4
85	Kristine	Wilkinson	kristine.wilkinson95@infotech.com	11	4
86	Joseph	Carter	joseph.carter78@infotech.com	9	3
87	Tammy	Martin	tammy.martin98@infotech.com	4	3
88	Chris	Lowe	chris.lowe47@infotech.com	12	2
89	Marc	Coleman	marc.coleman76@infotech.com	4	3
90	Priscilla	Ritter	priscilla.ritter77@infotech.com	1	2
91	Douglas	Sanchez	douglas.sanchez76@infotech.com	4	4
92	Jesse	Bray	jesse.bray43@infotech.com	9	2
93	Jesus	Walsh	jesus.walsh47@infotech.com	1	2
94	Robert	Jensen	robert.jensen24@infotech.com	9	5
95	Alexander	Gomez	alexander.gomez29@infotech.com	2	5
96	Karen	Green	karen.green45@infotech.com	10	5
97	Keith	Mitchell	keith.mitchell90@infotech.com	2	3
98	Anthony	Huber	anthony.huber29@infotech.com	5	5
99	Ryan	Wiley	ryan.wiley90@infotech.com	9	2
100	Whitney	Larson	whitney.larson3@infotech.com	4	3
101	Freddie	Jackson	freddie.jackson@infotech.com	3	2
\.


--
-- Data for Name: labor_categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.labor_categories (id, labor_code, labor_category, salary) FROM stdin;
1	SA1	System Administrator 1	50000.00
2	SA2	System Administrator 2	60000.00
3	SA3	System Administrator 3	70000.00
4	SE1	System Engineer 1	70000.00
5	SE2	System Engineer 2	90000.00
6	SE3	System Engineer 3	100000.00
7	SIE1	System Integration Engineer 1	80000.00
8	SIE2	System Integration Engineer 2	90000.00
9	SIE3	System Integration Engineer 3	100000.00
10	DEV1	Software Developer 1	100000.00
11	DEV2	Software Developer 2	150000.00
12	DEV3	Software Developer 3	200000.00
\.


--
-- Name: contracts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contracts_id_seq', 6, true);


--
-- Name: employees_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employees_id_seq', 101, true);


--
-- Name: labor_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.labor_categories_id_seq', 12, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: contracts contracts_contract_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts
    ADD CONSTRAINT contracts_contract_name_key UNIQUE (contract_name);


--
-- Name: contracts contracts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contracts
    ADD CONSTRAINT contracts_pkey PRIMARY KEY (id);


--
-- Name: employee_to_contracts employee_to_contracts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_to_contracts
    ADD CONSTRAINT employee_to_contracts_pkey PRIMARY KEY (employee_id, contract_id, labor_id);


--
-- Name: employees employees_email_address_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_email_address_key UNIQUE (email_address);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);


--
-- Name: labor_categories labor_categories_labor_category_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.labor_categories
    ADD CONSTRAINT labor_categories_labor_category_key UNIQUE (labor_category);


--
-- Name: labor_categories labor_categories_labor_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.labor_categories
    ADD CONSTRAINT labor_categories_labor_code_key UNIQUE (labor_code);


--
-- Name: labor_categories labor_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.labor_categories
    ADD CONSTRAINT labor_categories_pkey PRIMARY KEY (id);


--
-- Name: employee_to_contracts employee_to_contracts_contract_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_to_contracts
    ADD CONSTRAINT employee_to_contracts_contract_id_fkey FOREIGN KEY (contract_id) REFERENCES public.contracts(id);


--
-- Name: employee_to_contracts employee_to_contracts_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_to_contracts
    ADD CONSTRAINT employee_to_contracts_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employees(id);


--
-- Name: employee_to_contracts employee_to_contracts_labor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_to_contracts
    ADD CONSTRAINT employee_to_contracts_labor_id_fkey FOREIGN KEY (labor_id) REFERENCES public.labor_categories(id);


--
-- Name: employees employees_contract_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_contract_id_fkey FOREIGN KEY (contract_id) REFERENCES public.contracts(id);


--
-- Name: employees employees_labor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_labor_id_fkey FOREIGN KEY (labor_id) REFERENCES public.labor_categories(id);


--
-- PostgreSQL database dump complete
--

