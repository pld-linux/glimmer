Summary:	glimmer - simple code editor
Summary(pl):	glimmer - prosty edytor kodu ¼ród³owego
Name:		glimmer
Version:	1.2.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://download.sourceforge.net/glimmer/%{name}-%{version}.tar.gz
URL:		http://glimmer.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-vfs-devel > 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ORBit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	CodeCommander-devel
Obsoletes:	CodeCommander
Obsoletes:	latte

%define		_prefix		/usr/X11R6
%define		_pixmapsdir	%{_datadir}/pixmaps

%description
Glimmer is a simple text editing tool for editing nearly any type of
source code.

%description -l pl
Glimmer jest prostym narzêdziem s³u¿±cym do edycji kodu ¼ród³owego.

%prep
%setup -q

%build
rm -f missing aclocal.m4
%{__libtoolize}
aclocal -I macros
%{__autoconf}
%{__automake}
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
%{_datadir}/glimmer/languages
%{_datadir}/glimmer/scripts
%{_applnkdir}/Development/Editors/*
%{_pixmapsdir}/*
