Summary:	HTTP streaming server
Summary(pl.UTF-8):	Serwer HTTP obsługujący strumienie
Name:		sighttpd
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		Daemons
# trailing /%{name}-%{version}.tar.gz is a hack for df
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=sighttpd&openfile=%{name}-%{version}.tar.gz/%{name}-%{version}.tar.gz
# Source0-md5:	559036d49d92f8372624283aab022a44
URL:		https://oss.renesas.com/modules/document/?sighttpd
BuildRequires:	liboggz-devel >= 0.5.40
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_sysconfdir}

%description
Sighttpd is an HTTP streaming server designed for distributing
realtime input. It is particularly useful for making camera streams
available to multiple clients, and has been designed for embedded
systems use.

%description -l pl.UTF-8
Sighttpd to serwer strumieniowy HTTP, zaprojektowany do udostępniania
wejścia w czasie rzeczywistym. Jest przydatny szczególnie przy
udostępnianiu strumieni z kamer dla wielu klientów. Jest przeznaczony
głównie dla systemów wbudowanych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/sighttpd
%dir %{_sysconfdir}/sighttpd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sighttpd/sighttpd-720p.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sighttpd/sighttpd-multi.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sighttpd/sighttpd-oggstdin.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sighttpd/sighttpd-stdin-h264.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sighttpd/sighttpd-stdin-mjpeg.conf
%{_mandir}/man5/sighttpd.conf.5*
%{_mandir}/man8/sighttpd.8*
