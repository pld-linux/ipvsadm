/*
 *      IP Virtual Server
 *      data structure and functionality definitions
 */

#ifndef _IP_VS_H
#define _IP_VS_H

#include <asm/types.h>          /* For __uXX types */

#define IP_VS_VERSION_CODE            0x010007
#define NVERSION(version)                       \
	(version >> 16) & 0xFF,                 \
	(version >> 8) & 0xFF,                  \
	version & 0xFF

/*
 *      Virtual Service Flags
 */
#define IP_VS_SVC_F_PERSISTENT        0x0001    /* persistent port */
#define IP_VS_SVC_F_HASHED            0x0002    /* hashed entry */

/*
 *      Destination Server Flags
 */
#define IP_VS_DEST_F_AVAILABLE        0x0001    /* Available tag */

/*
 *      IPVS sync daemon states
 */
#define IP_VS_STATE_NONE    0           /* daemon is stopped */
#define IP_VS_STATE_MASTER  1           /* started as master */
#define IP_VS_STATE_BACKUP  2           /* started as backup */

/*
 *      IPVS socket options
 */
#define IP_VS_BASE_CTL		(64+1024+64)		/* base */

#define IP_VS_SO_SET_NONE	IP_VS_BASE_CTL	        /* just peek */
#define IP_VS_SO_SET_INSERT	(IP_VS_BASE_CTL+1)
#define IP_VS_SO_SET_ADD	(IP_VS_BASE_CTL+2)
#define IP_VS_SO_SET_EDIT	(IP_VS_BASE_CTL+3)
#define IP_VS_SO_SET_DEL	(IP_VS_BASE_CTL+4)
#define IP_VS_SO_SET_FLUSH	(IP_VS_BASE_CTL+5)
#define IP_VS_SO_SET_LIST	(IP_VS_BASE_CTL+6)
#define IP_VS_SO_SET_ADDDEST	(IP_VS_BASE_CTL+7)
#define IP_VS_SO_SET_DELDEST	(IP_VS_BASE_CTL+8)
#define IP_VS_SO_SET_EDITDEST	(IP_VS_BASE_CTL+9)
#define IP_VS_SO_SET_TIMEOUTS	(IP_VS_BASE_CTL+10)
#define IP_VS_SO_SET_STARTDAEMON (IP_VS_BASE_CTL+11)
#define IP_VS_SO_SET_STOPDAEMON (IP_VS_BASE_CTL+12)
#define IP_VS_SO_SET_RESTORE    (IP_VS_BASE_CTL+13)
#define IP_VS_SO_SET_SAVE       (IP_VS_BASE_CTL+14)
#define IP_VS_SO_SET_ZERO	(IP_VS_BASE_CTL+15)
#define IP_VS_SO_SET_MAX	IP_VS_SO_SET_ZERO

#define IP_VS_SO_GET_VERSION	IP_VS_BASE_CTL
#define IP_VS_SO_GET_INFO	(IP_VS_BASE_CTL+1)
#define IP_VS_SO_GET_SERVICES	(IP_VS_BASE_CTL+2)
#define IP_VS_SO_GET_SERVICE	(IP_VS_BASE_CTL+3)
#define IP_VS_SO_GET_DESTS	(IP_VS_BASE_CTL+4)
#define IP_VS_SO_GET_DEST	(IP_VS_BASE_CTL+5)	/* not used now */
#define IP_VS_SO_GET_TIMEOUTS	(IP_VS_BASE_CTL+6)
#define IP_VS_SO_GET_DAEMON	(IP_VS_BASE_CTL+7)
#define IP_VS_SO_GET_MAX	IP_VS_SO_GET_DAEMON


/*
 *      IPVS Connection Flags
 */
#define IP_VS_CONN_F_FWD_MASK         0x0007    /* mask for the fwd methods */
#define IP_VS_CONN_F_MASQ	      0x0000    /* masquerading */
#define IP_VS_CONN_F_LOCALNODE	      0x0001    /* local node */
#define IP_VS_CONN_F_TUNNEL	      0x0002    /* tunneling */
#define IP_VS_CONN_F_DROUTE           0x0003    /* direct routing */
#define IP_VS_CONN_F_BYPASS           0x0004    /* cache bypass */
#define IP_VS_CONN_F_HASHED	      0x0040	/* hashed entry */
#define IP_VS_CONN_F_NOOUTPUT         0x0080    /* no output packets */
#define IP_VS_CONN_F_INACTIVE         0x0100    /* not established */
#define IP_VS_CONN_F_OUT_SEQ          0x0200    /* must do output seq adjust */
#define IP_VS_CONN_F_IN_SEQ           0x0400    /* must do input seq adjust */
#define IP_VS_CONN_F_SEQ_MASK         0x0600    /* in/out sequence mask */
#define IP_VS_CONN_F_NO_CPORT         0x0800    /* no client port set yet */

/* Move it to better place one day, for now keep it unique */
#define NFC_IPVS_PROPERTY	0x10000

#define IP_VS_SCHEDNAME_MAXLEN         16
#define IP_VS_IFNAME_MAXLEN            16

struct ip_vs_rule_user {
	/* global options */
	int             tcp_timeout;    /* timeout values */
	int             tcp_fin_timeout;
	int             udp_timeout;
	int             state;          /* sync daemon state */
	char            mcast_ifn[IP_VS_IFNAME_MAXLEN];
					/* multicast interface name */

	/* virtual service options */
	u_int16_t	protocol;
	u_int32_t	vaddr;          /* virtual address */
	u_int16_t	vport;
	u_int32_t       vfwmark;        /* firwall mark of virtual service*/
	char            sched_name[IP_VS_SCHEDNAME_MAXLEN];
	unsigned	vs_flags;       /* virtual service flags */
	unsigned        timeout;        /* persistent timeout in ticks */
	u_int32_t	netmask;        /* persistent netmask */

	/* destination specific options */
	u_int32_t	daddr;          /* destination address */
	u_int16_t	dport;
	unsigned        conn_flags;     /* destination flags */
	int             weight;         /* destination weight */
};


/*
 *	IPVS statistics object (for user space)
 */
struct ip_vs_stats_user
{
	__u32                   conns;          /* connections scheduled */
	__u32                   inpkts;         /* incoming packets */
	__u32                   outpkts;        /* outgoing packets */
	__u64                   inbytes;        /* incoming bytes */
	__u64                   outbytes;       /* outgoing bytes */

	__u32			cps;		/* current connection rate */
	__u32			inpps;		/* current in packet rate */
	__u32			outpps;		/* current out packet rate */
	__u32			inbps;		/* current in byte rate */
	__u32			outbps;		/* current out byte rate */
};


/* The argument to IP_VS_SO_GET_INFO */
struct ip_vs_getinfo {
	/* version number */
	unsigned int	version;

	/* size of connection hash table */
	unsigned int	size;

	/* number of virtual services */
	unsigned int	num_services;
};

/* The argument to IP_VS_SO_GET_SERVICE */
struct ip_vs_service_user {
	/* which service: user fills this in */
	u_int16_t	protocol;
	u_int32_t	addr;           /* virtual address */
	u_int16_t	port;
	u_int32_t       fwmark;         /* firwall mark of virtual service */

	/* service options */
	char            sched_name[IP_VS_SCHEDNAME_MAXLEN];
	unsigned	flags;          /* virtual service flags */
	unsigned        timeout;        /* persistent timeout in ticks */
	u_int32_t	netmask;        /* persistent netmask */

	/* number of real servers */
	unsigned int    num_dests;

	/* statistics */
	struct ip_vs_stats_user stats;
};

struct ip_vs_dest_user {
	u_int32_t	addr;           /* destination address */
	u_int16_t	port;
	unsigned	flags;		/* destination flags */
	int		weight;         /* destination weight */
	u_int32_t	activeconns;	/* active connections */
	u_int32_t	inactconns;	/* inactive connections */

	/* statistics */
	struct ip_vs_stats_user stats;
};

/* The argument to IP_VS_SO_GET_DESTS */
struct ip_vs_get_dests {
	/* which service: user fills this in */
	u_int16_t	protocol;
	u_int32_t	addr;           /* virtual address */
	u_int16_t	port;
	u_int32_t       fwmark;         /* firwall mark of virtual service */

	/* number of real servers */
	unsigned int    num_dests;

	/* the real servers */
	struct ip_vs_dest_user entrytable[0];
};

/* The argument to IP_VS_SO_GET_SERVICES */
struct ip_vs_get_services {
	/* number of virtual services */
	unsigned int num_services;

	/* service table */
	struct ip_vs_service_user entrytable[0];
};

/* The argument to IP_VS_SO_GET_TIMEOUTS */
struct ip_vs_timeout_user {
	int             tcp_timeout;
	int             tcp_fin_timeout;
	int             udp_timeout;
};

/* The argument to IP_VS_SO_GET_DAEMON */
struct ip_vs_daemon_user {
	int	state;				/* sync daemon state */
	char	mcast_ifn[IP_VS_IFNAME_MAXLEN];	/* multicast interface name */
};

#endif	/* _IP_VS_H */
