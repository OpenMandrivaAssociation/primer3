%define build_with_tests	1

Name:		primer3
Version:	2.3.6
Release:	1
Summary:	PCR reactions primers identification
Group:		Sciences/Biology
License:	BSD and GPLv2+
URL:		https://primer3.sourceforge.net/
Source0:	http://downloads.sourceforge.net/primer3/%{name}-src-%{version}.tar.gz
Patch0:		primer3-2.2.3-linking.patch

%description
Primer3 is a complete rewrite of the original PRIMER program
(Primer 0.5), written by Steve Lincoln, Mark Daly, and Eric
Lander.

Primer3 picks primers for PCR reactions, considering as criteria:
- oligonucleotide melting temperature, size, GC content,
  and primer-dimer possibilities
- PCR product size
- positional constraints within the source sequence
- miscellaneous other constraints

All of these criteria are user-specifiable as constraints, and
some are specifiable as terms in an objective function that
characterizes an optimal primer pair.

%prep
%setup -q -n %{name}-%{version}
%patch0  -p1 -b .linking

%build
%make -C src CFLAGS="%{optflags} -D__USE_FIXED_PROTOTYPES__" LDFLAGS="%{ldflags}" V=1 

%install
install -Dpm 755 src/primer3_core %{buildroot}%{_bindir}/primer3_core
install -Dpm 755 src/ntdpal %{buildroot}%{_bindir}/ntdpal
install -Dpm 755 src/ntthal %{buildroot}%{_bindir}/ntthal
install -Dpm 755 src/oligotm %{buildroot}%{_bindir}/oligotm
install -Dpm 755 src/long_seq_tm_test %{buildroot}%{_bindir}/long_seq_tm_test

%if %build_with_tests
%check
%make -C test
%endif

%files
%doc *.txt *.htm example src/release_notes.txt
%{_bindir}/*


