Summary:	glimmer - simple code editor
Summary(pl):	glimmer - prosty edytor kodu �r�d�owego
Name:		glimmer
Version:	1.0.8
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://download.sourceforge.net/glimmer/%{name}-%{version}.tar.gz
URL:		http://glimmer.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	CodeCommander-devel
Obsoletes:	CodeCommander
Obsoletes:	latte

%define		_prefix		/usr/X11R6
%define		_pixmapsdir	%{_datadir}/pixmaps

%description
LATTE is a simple text editing tool for editing nearly any type of
source code.

%description -l pl
LATTE jest prostym narz�dziem s�u��cym do edycji kodu �r�d�owego.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-gnome \
	--disable-python

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Development/Editors

gzip -9nf AUTHORS TODO README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glimmer
%{_applnkdir}/Development/Editors/*
%{_pixmapsdir}/*
