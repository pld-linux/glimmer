Summary:	glimmer - simple code editor
Summary(pl):	glimmer - prosty edytor kodu ¼ród³owego
Name:		glimmer
Version:	1.0.1
Release:	1
LIcense:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://download.sourceforge.net/glimmer/%{name}-%{version}.tar.gz
URL:		http://glimmer.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	python-devel >= 2.0
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
LATTE jest prostym narzêdziem s³u¿±cym do edycji kodu ¼ród³owego.

%prep
%setup  -q

%build
CXXFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS -fno-rtti -fno-exceptions}"
%configure \
	--enable-gnome

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
