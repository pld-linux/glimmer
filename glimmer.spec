Summary:	glimmer - simple code editor
Summary(pl):	glimmer - prosty edytor kodu ¼ród³owego
Name:		glimmer
Version:	1.99.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
# Source0-md5:	59d6324bab435f85f73b1ffb93afdcfe
URL:		http://glimmer.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eel-devel >= 2.3.6
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtksourceview-devel >= 0.5.0
BuildRequires:	libbonoboui-devel >= 2.3.3
BuildRequires:	libgnomeprintui-devel >= 2.3.1
BuildRequires:	libgnomeui-devel >= 2.3.3
BuildRequires:	libtool
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2
Obsoletes:	CodeCommander
Obsoletes:	CodeCommander-devel
Obsoletes:	latte
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glimmer is a simple text editing tool for editing nearly any type of
source code.

%description -l pl
Glimmer jest prostym narzêdziem s³u¿±cym do edycji kodu ¼ród³owego.

%prep
%setup -q

%build
rm -f missing aclocal.m4
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Editors

%find_lang %{name}-too --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun -p /sbin/ldconfig

%files -f %{name}-too.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO NEWS
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/lib*.la
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/glimmer-ui.xml
%{_datadir}/idl/libglimmerfile-1.0
